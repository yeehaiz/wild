# coding: utf-8

from django.shortcuts import render
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

from event.models import Session, Event
from users.models import User
from users.service import user_info, get_frequent_members, save_frequent_members
from helpers import utils, decorators, errors
from order.service import get_event_fee, get_equipment_rent
from order.models import Order, OrderMember, OrderEquipment

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
    mobile = request.session.get('mobile')
    frequent_members = get_frequent_members(uid)
    contacts_name = {fm['mobile']: fm['name'] for fm in frequent_members}.get(mobile, '')
    equipments = [{
        'id': eqpmnt.id,
        'name': eqpmnt.name,
        'rent': eqpmnt.rent,
        'stock': eqpmnt.storage - eqpmnt.num_out,
    } for eqpmnt in session.event.equipments.all()]

    return render(request, 'fill.html', {
        'user': user_info(request),
        'contacts_name': contacts_name,
        'session': session,               # 场次
        'session_id': session_id,
        'num_apply': num_apply,
        'num_apply_range': range(1, 1+num_apply),
        'frequent_members': frequent_members,
        'equipments': equipments,
    })


@csrf_exempt
@decorators.login
@decorators.jsonapi
@transaction.atomic
def submit(request):
    # 输入
    person_rules = [
        ('name', 'person_name',           lambda v: (v if 2<=len(v)<=10 else None), '请填写正确的姓名'),
        ('mobile', 'person_phone',         lambda v: (v if utils.is_mobile(v) else None ), '请填写正确的手机号'),
        ('cert_type', 'credentials_type', lambda v: (int(v) if int(v) == 1 else None), '证件类型错误'),
        ('cert', 'credentials_no',        lambda v: (v if utils.checkIdcard(v)[0] else None), '请填写正确的证件号'),
        ('sex', 'person_sex',             lambda v: (v if v in ['f', 'm'] else None), '请选择性别'),
        ('birthday', 'person_birthday',   lambda v: (utils.date_strp(v)), '请填写正确的生日'),
    ]
    try:
        session_id = int(request.POST.get('session_id'))
        num_apply = int(request.POST.get('num_apply'))
        assert num_apply > 0
    except:
        raise errors.ApiError('提交数据有误')

    # 场次操作
    session = Session.objects.select_for_update().filter(id=session_id)
    if session:
        session = session[0]
    else:
        raise errors.ApiError('您报名的活动场次不存在')

    if session.start_dt <= datetime.date.today():
        raise errors.ApiError('您报名的活动场次已过期')

    if session.event.places < session.num_apply + num_apply:
        raise errors.ApiError('该场次剩余名额为%d，名额不足' % session.event.places - session.num_apply)

    session.num_apply += num_apply
    session.save()

    # 表单信息获取校验
    persons = []
    for i in xrange(1, num_apply+1):
        p = {}
        for bname, fname, transf, errmsg in person_rules:
            try:
                p[bname] = transf( request.POST.get('%s_%d'%(fname, i), '').strip() )
                assert p[bname]
            except Exception as e:
                raise errors.ApiError(errmsg)

        persons.append(p)

    contacts_name = request.POST.get('contacts_name', '').strip()
    if not (2<=len(contacts_name) <=10) :
        raise errors.ApiError('请填写正确的性名')
    contacts_mobile = request.POST.get('contacts_mobile', '').strip()
    if not utils.is_mobile(contacts_mobile):
        raise errors.ApiError('请填写正确的手机号')
    comment = request.POST.get('postscript', '')

    # 装备操作
    equipments = session.event.equipments.select_for_update().all()
    equip_rent = {}
    for eqpmnt in equipments:
        rent_cnt = request.POST.get('equipment_%d' % eqpmnt.id, '0')
        rent_cnt = utils.parseInt(rent_cnt) or 0
        equip_rent[eqpmnt.id] = rent_cnt

        if eqpmnt.storage < eqpmnt.num_out + rent_cnt:
            raise errors.ApiError('装备【%s】剩余数量为%d，数量不足' % (eqpmnt.name, eqpmnt.storage - eqpmnt.num_out))
        eqpmnt.num_out += rent_cnt
        eqpmnt.save()

    # 订单创建
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    order = Order(user = user,
                  session = session,
                  number = num_apply,
                  contact_name = contacts_name,
                  contact_mobile = contacts_mobile,
                  comment = comment,
                  apply_fee = get_event_fee(session.event, persons),
                  equipment_rent = get_equipment_rent(equipments, equip_rent))
    order.save()

    for p in persons:
        ordermember = OrderMember(order = order,
                                  name = p['name'],
                                  mobile = p['mobile'],
                                  cert_type = p['cert_type'],
                                  cert = p['cert'],
                                  sex = p['sex'],
                                  birthday = p['birthday'])
        ordermember.save()

    for eqpmnt in equipments:
        if equip_rent[eqpmnt.id] > 0:
            orderequipment = OrderEquipment(order = order,
                                        equipment = eqpmnt,
                                        number = equip_rent[eqpmnt.id])
            orderequipment.save()

    # 保存常用联系人
    save_frequent_members(user, persons)

    return {'url': '/order/pay/%d/' % order.id}
