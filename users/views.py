# coding: utf-8

import json

from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q

from users.models import (User, Admin, FrequentMember)
from users.service import user_info, get_cert_type, get_sex
from users import constants
from helpers import errors, decorators, utils, verifycode
from order.models import Order, OrderMember, OrderEquipment
from order.service import get_order_status

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user_objects = User.objects.filter(Q(mobile=username) | Q(username=username))
        if not user_objects:
            return render(request, 'login.html', {
                'user': user_info(request),
                'data': {
                    'username': username,
                    'errmsg': '用户不存在',
                }
            })

        user = user_objects[0]
        if user.password != utils.md5(password):
            return render(request, 'login.html', {
                'user': user_info(request),
                'data': {
                    'username': username,
                    'errmsg': '密码错误',
                }
            })

        # 登录成功
        user_admin = Admin.objects.filter(user_id=user.id)
        request.session['admin'] = user_admin[0].level if user_admin else 0
        request.session['uid'] = user.id
        request.session['username'] = user.username
        request.session['mobile'] = user.mobile

        redirectURL = request.GET.get('redirectURL')
        return HttpResponseRedirect(redirectURL or '/')


def logout(request):
    if 'admin' in request.session:
        del request.session['admin']
    if 'uid' in request.session:
        del request.session['uid']
    if 'username' in request.session:
        del request.session['username']
    if 'mobile' in request.session:
        del request.session['mobile']

    return HttpResponseRedirect('/')


def register(request):
    return render(request, 'register.html', {})


@decorators.jsonapi
def register_check_username(request):
    username = request.GET.get('username', '')
    if not utils.is_username(username):
        raise errors.ApiError(constants.RULE_USERNAME)

    if User.objects.filter(username=username).count() > 0:
        raise errors.ApiError('该用户名已被注册')

    return None


@csrf_exempt
@decorators.jsonapi
def sendverifycode(request):
    mobile = request.POST.get('mobile', '')

    if not utils.is_mobile(mobile):
        raise errors.ApiError('无效的手机号')

    if User.objects.filter(mobile=mobile).count() > 0:
        raise errors.ApiError('手机号已存在')

    success, reason = verifycode.send_vcode(request, mobile, constants.MSG_REGISTER_VERIFY_CODE)
    if not success:
        raise errors.ApiError(reason)

    return None


@decorators.jsonapi
def register_post(request):
    username = request.POST.get('username', '')
    mobile = request.POST.get('mobile', '')
    password = request.POST.get('password', '')
    vcode_str = request.POST.get('vcode', '0')

    if not utils.is_username(username):
        raise errors.ApiError(constants.RULE_USERNAME)

    if User.objects.filter(username=username).count() > 0:
        raise errors.ApiError('该用户名已被注册')

    if not utils.is_mobile(mobile):
        raise errors.ApiError('无效的手机号')

    if User.objects.filter(mobile=mobile).count() > 0:
        raise errors.ApiError('该手机号已被注册')

    try:
        vcode = int(vcode_str)
    except ValueError:
        raise errors.ApiError('请输入正确的验证码')

    success, reason = verifycode.verify(mobile, vcode)
    if not success:
        raise errors.ApiError(reason)

    if not utils.is_valid_password(password):
        raise errors.ApiError('密码不符合规范')

    # 验证成功, 创建用户
    user = User()
    user.username = username
    user.mobile = mobile
    user.password = utils.md5(password)
    user.save()

    # 设置session
    user_admin = Admin.objects.filter(user_id=user.id)
    request.session['admin'] = user_admin[0].level if user_admin else 0
    request.session['uid'] = user.id
    request.session['username'] = user.username

    return None

@decorators.login
def myorders(request):
    uid = request.session['uid']
    orders = [
        {
            'status_str': get_order_status(order.status),
            'picture': json.loads(order.session.event.covers)[0],
            'cre_time': utils.tsf(order.cre_time),
            'o': order,
        } for order
        in Order.objects.filter(user_id=uid).order_by('-upd_time')
    ]
    return render(request, 'myorders.html', {
        'user': user_info(request),
        'orders': orders,
    });

@decorators.login
def mycontacts(request):
    uid = request.session['uid']
    contacts = [
        {
            'c': c,
            'cert_type': get_cert_type(c.cert_type),
            'sex': get_sex(c.sex),
        } for c
        in FrequentMember.objects.filter(user_id=uid)
    ]

    return render(request, 'mycontacts.html', {
        'user': user_info(request),
        'contacts': contacts,
    });
