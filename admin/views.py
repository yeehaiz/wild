# coding: utf-8

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

from event.models import Event, Session, Equipment
from order.models import Order, OrderEquipment, OrderMember
from users.service import user_info
from event.service import get_eventtype_name, get_eventtype_list
from helpers import utils, snfs, decorators, errors

from .forms import EventSaveForm

import math
import json

PAGESIZE = 20
NAVCOUNT = 11


@decorators.admin()
def events(request):
    page = int(request.GET.get('page', 1))
    event_objects = Event.objects.order_by('-upd_time', 'id')[(page-1)*PAGESIZE: page*PAGESIZE]
    events = [{
        'id': event.id,
        'title': event.title,
        'type' : get_eventtype_name(event.type_id),
        'days' : event.days,
        'price': event.price,
        'session_count': event.session_set.count(),
        'cre_time' : str(event.cre_time),
    } for event in event_objects]

    event_count = Event.objects.count()
    page_count = int(math.ceil(1.0 * event_count / PAGESIZE))

    return render(request, 'events.html', {
        'user': user_info(request),
        'events': events,
        'page': {
            'prev' : max(1, page -1),
            'next' : min(page_count, page + 1),
            'range' : utils.paging_range(page, page_count, NAVCOUNT),
            'current' : page,
        }
    })


@decorators.admin()
def events_add(request):
    types = get_eventtype_list()

    return render(request, 'events_edit.html', {
        'types': types,
        'intensity': range(1, 6),
        'covers': '[]',
    })


@decorators.admin()
def events_update(request, event_id):
    types = get_eventtype_list()

    event = get_object_or_404(Event, id=event_id)

    return render(request, 'events_edit.html', {
        'types': types,
        'intensity': range(1, 6),
        'covers': event.covers,
        'event': event,
    })




@decorators.admin()
@decorators.jsonapi
def events_save(request):
    form = EventSaveForm(request.POST)
    if not form.is_valid():
        raise errors.ApiError('数据错误')

    covers = request.POST.getlist('covers')
    if not covers:
        raise errors.ApiError('无图片')

    if  form.cleaned_data['id']:
        event = Event.objects.get(id=form.cleaned_data['id'])
        event.upd_user_id = request.session.get('uid', 0)
    else:
        event = Event()
        event.cre_user_id = request.session.get('uid', 0)
        event.upd_user_id = request.session.get('uid', 0)

    try:
        event.title = form.cleaned_data['title']
        event.type_id = form.cleaned_data['type_id']
        event.intensity = form.cleaned_data['intensity']
        event.days = form.cleaned_data['days']
        event.places = form.cleaned_data['places']
        event.price = form.cleaned_data['price']
        event.covers = json.dumps(covers)
        event.outline = form.cleaned_data['outline']
        event.route = form.cleaned_data['route']
        event.planning = form.cleaned_data['planning']
        event.fee_desc = form.cleaned_data['fee_desc']
        event.equipment = form.cleaned_data['equipment']
        event.save()

    except Exception as e:
        raise errors.ApiError('存储失败: ' + e.message)

    return None


@decorators.admin()
def sessions(request, event_id):
    event = Event.objects.get(id=event_id)

    sessions = [
        {
            'id': sess.id,
            'start_dt': str(sess.start_dt),
            'end_dt': utils.df(utils.date_add(sess.start_dt, sess.event.days)),
            'num_apply': sess.num_apply,
            'cre_time': str(sess.cre_time),
            'auto': sess.auto,
        } for sess
        in Session.objects.filter(event_id=event_id).order_by('-start_dt')
    ]


    return render(request, 'sessions.html', {
        'user': user_info(request),
        'sessions': sessions,
        'event': event,
    })


@decorators.admin()
def sessions_add(request):
    event_id = request.POST.get('event_id')
    start_dt = request.POST.get('start_dt')

    sess = Session()
    sess.event = Event.objects.get(id=event_id)
    sess.start_dt = start_dt

    sess.save()

    return HttpResponseRedirect('/admin/sessions/' + event_id + '/')

@decorators.admin()
def sessions_delete(request, session_id):
    sess = Session.objects.get(id=session_id)
    if sess.num_apply > 0:
        return HttpResponse('已有人报名, 无法删除')

    sess.delete()
    return HttpResponseRedirect('/admin/events/')


@csrf_exempt
@decorators.admin()
def uploadimage(request):
    file = request.FILES.get('file')
    if not file:
        return HttpResponse()

    imgurl = snfs.save_request_file(file)

    return HttpResponse(imgurl)




@decorators.admin()
def sessions_orders(request, sid):
    orders = [
        {
            'id': order.id,
            'username': order.user.username,
            'contact_name': order.contact_name,
            'contact_mobile': order.contact_mobile,
            'male_num': order.ordermember_set.filter(sex='m').count(),
            'female_num': order.ordermember_set.filter(sex='f').count(),
            'total': order.total,
            'cre_date': str(order.cre_time.date()),
            'status': order.status,
        }
        for order in Order.objects.filter(session_id=int(sid), status__gt=0).order_by('status', 'cre_time')
    ]

    return render(request, 'orders.html', {
        'user': user_info(request),
        'orders': orders,
    })

@decorators.admin()
@decorators.jsonapi
@transaction.atomic
def orders_status(request):
    oid = int(request.GET.get('oid'))
    status = int(request.GET.get('status'))
    assert status in [1,2,3,4,5]
    order = Order.objects.get(id=oid)

    # 装备状态修改
    if order.status == 4 and status != 4:
        for equip in order.orderequipment_set.all():
            equip.status = 0
            equip.save()

    if order.status != 4 and status == 4:
        for equip in order.orderequipment_set.all():
            equip.status = 1
            equip.save()

    order.status = status
    order.save()
    return {'msg': 'success'}

@decorators.admin()
@decorators.jsonapi
@transaction.atomic
def auto_approve(request):
    sid = int(request.GET.get('sid'))
    auto = int(request.GET.get('auto'))
    auto = bool(auto)
    session = Session.objects.get(id=sid)
    session.auto = auto
    session.save()
    return {'msg': 'success'}


@decorators.admin()
def equipments(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipments.html', {
        'user': user_info(request),
        'equipments': equipments,
    })
