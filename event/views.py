from django.shortcuts import render
from django.http import HttpResponse

from event.models import Event

from . import service
from users.service import user_info

import json


def lists(request):

    events = Event.objects.all()

    data = [{
        'id': event.id,
        'title': event.title,
        'type': event.type.name,
        'intensity': range(event.intensity),
        'days': event.days,
        'price': int(event.price),
        'cover': json.loads(event.covers)[0],
        'outline': event.outline,

    } for event in events]

    return render(request, 'lists.html', {
        'user': user_info(request),
        'events': data,
    })



def lists2(request):

    return render(request, 'lists2.html', {'name': 'hello'})


def detail2(request):

    return render(request, 'detail2.html', {'name': 'hello'})


def detail(request, event_id):
    event = Event.objects.get(id=event_id)
    data = {
        'id': event.id,
        'title': event.title,
        'type': event.type.name,
        'intensity': range(event.intensity),
        'days': event.days,
        'places': event.places,
        'price': event.price,
        'covers': json.loads(event.covers),
        'outline': event.outline,
        'route': event.route,
        'planning': service.planning_parse(event.planning),
        'fee_desc': service.text_parse(event.fee_desc),
        'equipment': service.text_parse(event.equipment),
    }


    return render(request, 'detail.html', {
        'user': user_info(request),
        'event': data,
    })
