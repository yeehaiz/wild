from django.shortcuts import render

from event.models import Event, EventType
from users.service import user_info
from helpers import utils

import math

PAGESIZE = 20
NAVCOUNT = 11



def events(request):
    page = int(request.GET.get('page', 1))
    event_objects = Event.objects.order_by('-cre_time', 'id')[(page-1)*PAGESIZE: page*PAGESIZE]
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


    if request.method == 'GET':
        return render(request, 'events_edit.html', {
            'types': types,
            'intensity': range(5),
        })
