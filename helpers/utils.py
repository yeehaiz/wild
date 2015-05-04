import re
import datetime
import hashlib


REG_MOBILE = re.compile(r'1[34578]{1}\d{9}$')
REG_USERNAME = re.compile(r'[a-zA-Z][a-z0-9A-Z_]{2,}$')

def md5(s):
    hash_md5 = hashlib.md5(s)
    return hash_md5.hexdigest()


def is_mobile(mobile):
    return bool(REG_MOBILE.match(mobile))


def is_username(username):
    return bool(REG_USERNAME.match(username))


def get_client_ip(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']



def paging_range(current, page_count, nav_count):
    if page_count <= nav_count:
        return range(1, page_count+1)

    start = current - nav_count/2
    end = start + nav_count

    if start < 1:
        return range(1, 1 + nav_count)

    if end > nav_count + 1:
        return range(page_count - nav_count + 1 , page_count + 1)

    return range(start, end)



## date functions

def df(dt):
    '''date format'''
    return dt.strftime('%Y-%m-%d')

def date_add(dt, days):
    return (dt +  datetime.timedelta(days))

def month_begin_add(dt, months):
    m = (dt.month + months - 1) % 12 + 1
    y = dt.year + (dt.month + months -1) /12
    return datetime.date(y, m, 1)

def month_end_add(dt, months):
    m = (dt.month + months) % 12 + 1
    y = dt.year + (dt.month + months) /12
    return datetime.date(y, m, 1) - datetime.timedelta(1)
