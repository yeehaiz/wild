from django.shortcuts import render
from django.http import HttpResponse

from event.models import Event


from . import service
from . import constants
from users.service import user_info
from helpers import utils

import json
import math
import datetime

def lists(request):

    page = int(request.GET.get('page', '1'))
    event_type_id = int(request.GET.get('type', '0'))
    peroid_type_id = int(request.GET.get('peroid', '0'))

    events = service.list_get_events(page, event_type_id, peroid_type_id)
    event_count = service.list_get_count(event_type_id, peroid_type_id)

    data = [{
        'id': event['id'],
        'title': event['title'],
        'type': service.get_eventtype_name(event['type_id']),
        'intensity': range(event['intensity']),
        'days': event['days'],
        'price': int(event['price']),
        'cover': json.loads(event['covers'])[0],
        'outline': event['outline'],

    } for event in events]


    return render(request, 'lists.html', {
        'user': user_info(request),
        'events': data,
        'page': service.list_page_nav(page, event_count),
        'event_types': service.get_eventtype_list(),
        'peroid_types': constants.get_peroid_types(),
        'filter': {
            'event_type_id': event_type_id,
            'peroid_type_id': peroid_type_id,
        },
    })





def lists2(request):

    return render(request, 'lists2.html', {'name': 'hello'})


def detail2(request):

    return render(request, 'detail2.html', {'name': 'hello'})


def detail(request, event_id):
    event = Event.objects.get(id=event_id)
    sessions = event.session_set.filter(start_dt__gt=datetime.date.today()).order_by('start_dt')
    sesses = [
        {
            'session_id': sess.id,
            'date_desc': utils.df_week(sess.start_dt),
            'places': sess.event.places - sess.num_apply,

        } for sess in sessions
        if sess.num_apply < sess.event.places
    ]


    data = {
        'id': event.id,
        'title': event.title,
        'type': service.get_eventtype_name(event.type_id),
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
        'sesses': sesses,
    }


    return render(request, 'detail.html', {
        'user': user_info(request),
        'event': data,
    })
