# coding: utf-8

from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q

from users.models import (User, Admin)
from users.service import user_info
from helpers import utils


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
