# coding: utf-8

from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from event.models import Event, EventType
from users.service import user_info
from helpers import utils, snfs, decorators, errors

from .forms import EventSaveForm

import math
import json

PAGESIZE = 20
NAVCOUNT = 11


#@decorators.admin()
def events(request):
    page = int(request.GET.get('page', 1))
    event_objects = Event.objects.order_by('-upd_time', 'id')[(page-1)*PAGESIZE: page*PAGESIZE]
    events = [{
        'id': event.id,
        'title': event.title,
        'type' : event.type.name,
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


def events_add(request):
    types = EventType.objects.filter(is_active=True).order_by('-sort')

    return render(request, 'events_edit.html', {
        'types': types,
        'intensity': range(1, 6),
        'covers': '[]',
    })


def events_update(request, event_id):
    types = EventType.objects.filter(is_active=True).order_by('-sort')

    event = get_object_or_404(Event, id=event_id)

    return render(request, 'events_edit.html', {
        'types': types,
        'intensity': range(1, 6),
        'covers': event.covers,
        'event': event,
    })




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
        event.type = EventType.objects.get(id=form.cleaned_data['type_id'])
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



@csrf_exempt
#@decorators.admin()
def uploadimage(request):
    file = request.FILES.get('file')
    if not file:
        return HttpResponse()

    imgurl = snfs.save_request_file(file)

    return HttpResponse(imgurl)
