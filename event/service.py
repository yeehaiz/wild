# coding: utf-8

from django.db import connection
from event.models import Event
from event import constants


from helpers import utils
import math


EVENT_TYPES_MAP = {
    i['id']: i for i in constants.EVENT_TYPES
}




def list_get_events(page, event_type_id, peroid_type_id):

    peroid_type = filter(lambda x: x['id'] == peroid_type_id,  constants.get_peroid_types())[0]
    peroid_where = peroid_type['where']

    query = '''
    select
      evn.*
    from event_event evn
    where %(type_where)s
    and evn.id in
    (
       select event_id from event_session sess where %(peroid_where)s
    )
    order by cre_time DESC
    limit %(limit)d
    offset %(offset)d
    ''' % {
        'type_where': 'evn.type_id = %d' % event_type_id if event_type_id else '1=1',
        'peroid_where': peroid_where if peroid_where else '1=1',
        'offset': (page-1) * constants.LIST_PAGE_SIZE,
        'limit': constants.LIST_PAGE_SIZE,
    }


    cursor = connection.cursor()
    cursor.execute(query)

    data = []
    for row in cursor:
        data.append({
            'id': row[0],
            'title': row[1],
            'intensity': row[2],
            'days': row[3],
            'places': row[4],
            'price': row[5],
            'covers': row[6],
            'outline': row[7],
            'route': row[8],
            'planning': row[9],
            'fee_desc': row[10],
            'equipment': row[11],
            'cre_time': row[12],
            'cre_user_id': row[13],
            'upd_time': row[14],
            'upd_user_id': row[15],
            'type_id': row[16],
        })

    return data;


def list_get_count(event_type_id, peroid_type_id):
    peroid_type = filter(lambda x: x['id'] == peroid_type_id,  constants.get_peroid_types())[0]
    peroid_where = peroid_type['where']

    query = '''
    select
      evn.*
    from event_event evn
    where %(type_where)s
    and evn.id in
    (
       select event_id from event_session sess where %(peroid_where)s
    )

    ''' % {
        'type_where': 'evn.type_id = %d' % event_type_id if event_type_id else '1=1',
        'peroid_where': peroid_where if peroid_where else '1=1',
    }


    cursor = connection.cursor()
    return cursor.execute(query)




def list_page_nav(page, count):
    page_count = int(math.ceil(1.0 * count / constants.LIST_PAGE_SIZE))

    return {
        'prev' : max(1, page -1),
        'next' : min(page_count, page + 1),
        'range' : utils.paging_range(page, page_count, constants.LIST_NAV_COUNT),
        'current' : page,
    }



def get_eventtype_list():
    return filter(lambda x: x['is_active'], constants.EVENT_TYPES)

def get_eventtype_name(event_type_id):
    event_type = EVENT_TYPES_MAP.get(event_type_id)
    return event_type['name'] if event_type else ''


def planning_parse(planning):
    plans = []
    for line in _x_format_lines(planning):
        if line.startswith('@'):
            plans.append({
                'title': line[1:].strip(),
                'lines': [],
            })
        elif plans:
            plans[-1]['lines'].append(line)

    data = []
    for plan in plans:
        data.append({
            'title': plan['title'],
            'paragraphs': list(_x_paragraphs(plan['lines'])),
        })

    return data


def text_parse(text):
    return list(_x_paragraphs(_x_format_lines(text)))




def _x_format_lines(text):
    prev = None
    for line in text.splitlines():
        trim = line.strip()
        if trim or prev:
            yield trim
        prev = trim

def _x_paragraphs(lines):
    parag = []
    prev = None
    for line in lines:
        if line:
            parag.append(line)
        elif prev:
            yield parag
            parag = []
        prev = line

    if parag:
        yield parag
