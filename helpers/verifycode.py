# coding: utf-8

import datetime
import random
from users.models import VerifyCode
from helpers import utils, smss


MOBILE_RESTRICT = (datetime.timedelta(minutes=30), 5)
IP_RESTRICT = (datetime.timedelta(minutes=30), 10)

VCODE_EXPIRE_TIME = datetime.timedelta(minutes=30)
VCODE_MAX_VERIRY_COUNT = 5


def generate_vcode():
    random.randint(100000, 999999)


def send_vcode(request, mobile, msg_template):
    '''
    @param mobile: 手机
    @param msg_template: 消息模板, 其中%(vcode)d 代表验证码
    @return (success, reason)
    '''
    ip = utils.get_client_ip(request)

    if not utils.is_mobile(mobile):
        return False, '无效手机号'

    now = datetime.datetime.now()
    # mobile restrict
    count = VerifyCode.objects.filter(mobile=mobile,
                cre_time__gt = now - MOBILE_RESTRICT[0]).count()
    if count >= MOBILE_RESTRICT[1]:
        return False, '验证码请求过于频繁'

    # ip restrict
    count = VerifyCode.objects.filter(ip=ip,
                cre_time__gt = now - IP_RESTRICT[0]).count()
    if count >= IP_RESTRICT[1]:
        return False, '验证码请求过于频繁'

    # send
    vcode = generate_vcode()
    msg = msg_template % {'vcode': vcode}
    smss.send(mobile, msg)

    verify_code = VerifyCode()
    verify_code.mobile = mobile
    verify_code.vcode = vcode
    verify_code.ip = ip
    verify_code.save()

    return True, '发送成功'


def verify(mobile, vcode):
    '''
    @return (success, reason)
    '''
    expire_time = datetime.datetime.now() - VCODE_EXPIRE_TIME
    vcs = VerifyCode.filter(mobile=mobile, cre_time__gt=expire_time).order_by('-cre_time')[:1]
    if not vcs:
        return False, '请重新获取验证码'

    vc = vsc[0]
    if vc.vtimes >= VCODE_MAX_VERIRY_COUNT:
        return False, '请重新获取验证码'

    if vc.vcode != vcode:
        vc.vtimes += 1
        vc.save()
        return False, '验证码错误'

    return True, '验证成功'
