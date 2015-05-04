# coding: utf-8

from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q

from users.models import (User, Admin)
from users.service import user_info
from users import constants
from helpers import errors, decorators, utils, verifycode


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
                    'errmsg': '密码错误',
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

        redirectURL = request.GET.get('redirectURL')
        return HttpResponseRedirect(redirectURL or '/')


def logout(request):
    if 'admin' in request.session:
        del request.session['admin']
    if 'uid' in request.session:
        del request.session['uid']
    if 'username' in request.session:
        del request.session['username']

    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {})

    if request.method == 'POST':
        pass


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

    return null

@decorators.jsonapi
def post_register(request):
    username = request.POST.get('username', '')
    mobile = request.POST.get('mobile', '')
    password = request.POST.get('password', '')
    vcode = request.POST.get('vcode', '0')

    if not utils.is_username(username):
        raise errors.ApiError('用户名不符合要求')

    if User.objects.filter(username=username).count() > 0:
        raise errors.ApiError('用户名已存在')

    if not utils.is_mobile(mobile):
        raise errors.ApiError('无效的手机号')

    if User.objects.filter(mobile=mobile).count() > 0:
        raise errors.ApiError('手机号已存在')

    success, reason = verifycode.verify(mobile, vcode)
    if not success:
        raise errors.ApiError(reason)
