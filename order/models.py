# coding: utf-8

from django.db import models

from users.models import User
from event.models import Session, Equipment

class Order(models.Model):
    ORDER_STATUSES = ((0, '待支付'), (1, '已支付'), (-1, '已取消'), (-2, '已退款'))
    EQPMNT_STATUSES = ((0, '待取'), (1, '借出'), (2, '完成'))

    user = models.ForeignKey(User, verbose_name='用户')
    session = models.ForeignKey(Session, verbose_name='场次')
    number = models.IntegerField('人数')
    contact_name = models.CharField('联系人姓名', max_length=16)
    contact_mobile = models.CharField('联系人手机', max_length=16)
    comment = models.CharField('备注', max_length=512)

    apply_fee= models.DecimalField('报名费', max_digits=9, decimal_places=2)
    equipment_rent = models.DecimalField('装备租金', max_digits=9, decimal_places=2)

    equipment_status = models.IntegerField('装备状态', choices=EQPMNT_STATUSES, default=0)
    status = models.IntegerField('订单状态', choices=ORDER_STATUSES, default=0)
    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('更新时间', auto_now=True)


class OrderMember(models.Model):
    CERT_TYPES = ((1, '身份证'), (2, '护照'), (3, '军官证'), (4, '回乡证'))
    SEX_CHOICES = (('m', '男'), ('f', '女'))

    order = models.ForeignKey(Order, verbose_name='订单')
    name = models.CharField('姓名', max_length=16)
    mobile = models.CharField('手机', max_length=16)
    cert_type = models.IntegerField('证件类型', choices=CERT_TYPES)
    cert = models.CharField('证件号', max_length=32)
    sex = models.CharField('性别', max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField('生日')


class OrderEquipment(models.Model):
    order = models.ForeignKey(Order, verbose_name='订单')
    equipment = models.ForeignKey(Equipment, verbose_name='装备')
    number = models.IntegerField('数量')
