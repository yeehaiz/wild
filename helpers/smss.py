# coding: utf-8

from django.conf import settings

from helpers import errors
import urllib, urllib2
import json


def send(mobile, msg):
    try:

        encodedata = urllib.urlencode({
            'apikey': settings.SMSS['apikey'],
            'mobile': mobile,
            'text': msg,
        })
        req = urllib2.Request(settings.SMSS['url'], encodedata)
        resp = urllib2.urlopen(req)
        ret_str = resp.read()
        data = json.loads(ret_str)

    except urllib2.HTTPError, e:
        raise errors.ApiError('短信接口调用失败')
    except urllib2.URLError, e:
        raise errors.ApiError('短信接口调用失败')
    except ValueError:
        raise errors.ApiError('短信接口调用失败')

    if data['code'] > 0:
        raise errors.ApiError('短信发送失败')
