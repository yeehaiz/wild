# coding: utf-8

'''
decorators
'''
from django.http.response import (
    HttpResponseForbidden,
    HttpResponseRedirect,
)


def admin(level = 1):
    def _deco(func):
        def _wrapper(request, *tuple_args, **dict_args):
            if request.session.get('admin') < level:
                return HttpResponseForbidden('管理员权限不够')
            return apply(func, (request,)+tuple_args, dict_args)
        return _wrapper
    return _deco


def login():
    def _deco(func):
        def _wrapper(request, *tuple_args, **dict_args):
            if request.session.get('uid') <= 0:
                return HttpResponseRedirect('/user/login/?redirectURL=' + request.path)
            return apply(func, (request,)+tuple_args, dict_args)
        return _wrapper
    return _deco
