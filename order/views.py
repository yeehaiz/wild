# coding: utf-8

from django.shortcuts import render

from event.models import Session, Event
from users.service import user_info, get_frequent_members
from helpers import utils, decorators

import datetime


@decorators.login
def fill(request):
    session_id = request.GET.get('session_id')
    num_apply = request.GET.get('num_apply')

    try:
        session_id = int(session_id)
        session = Session.objects.get(id=session_id)
    except:
        return render(request, 'error_info.html', {
            'user': user_info(request),
            'error': '该活动场次不存在',
        })

    try:
        num_apply = int(num_apply)
        assert 0 < num_apply <= session.event.places - session.num_apply
    except:
        return render(request, 'error_info.html', {
            'user': user_info(request),
            'error': '该场次剩余名额不足',
        })

    if session.start_dt <= datetime.date.today():
        return render(request, 'error_info.html', {
            'user': user_info(request),
            'error': '改活动已停止报名',
        })

    uid = request.session.get('uid')

    return render(request, 'fill.html', {
        'user': user_info(request),
        'session': session,
        'session_id': session_id,
        'num_apply_range': range(1, 1+num_apply),
        'frequent_members': get_frequent_members(uid),

    })
