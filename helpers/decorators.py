# coding: utf-8

'''
decorators
'''
from django.http.response import (
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseRedirect,
)

from helpers.errors import ApiError

import json


def admin(level = 1):
    def _deco(func):
        def _wrapper(request, *tuple_args, **dict_args):
            if request.session.get('admin') < level:
                return HttpResponseForbidden('管理员权限不够')
            return apply(func, (request,)+tuple_args, dict_args)
        return _wrapper
    return _deco


def login(func):
    def _wrapper(request, *tuple_args, **dict_args):
        if request.session.get('uid') <= 0:
            return HttpResponseRedirect('/user/login/?redirectURL=' + request.path)
        return apply(func, (request,)+tuple_args, dict_args)

    return _wrapper



def jsonapi(func):
    def _wrapper(request, *tuple_args, **dict_args):
        try:
            data = apply(func, (request,)+tuple_args, dict_args)

        except ApiError as e:
            response_data = {
                'code': e.code,
                'msg': e.msg,
                'data': None,
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        response_data = {
            'code': 0,
            'msg': '',
            'data': data,
        }
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    return _wrapper
