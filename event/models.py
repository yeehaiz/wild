# coding: utf-8

from django.db import models



class Equipment(models.Model):
    name = models.CharField('装备名', max_length=16)
    rent = models.DecimalField('租金', max_digits=9, decimal_places=2)
    price = models.DecimalField('价格', max_digits=9, decimal_places=2)
    storage = models.IntegerField('库存数量')
    num_out = models.IntegerField('借出数量')

    is_active = models.BooleanField('是否有效', default=True)
    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('修改时间', auto_now=True)


class Event(models.Model):
    title = models.CharField('标题', max_length=64)
    type_id = models.IntegerField('活动类型')
    intensity = models.IntegerField('活动强度')
    days = models.IntegerField('活动天数')
    places = models.IntegerField('名额')
    price = models.DecimalField('价格', max_digits=9, decimal_places=2)

    covers = models.TextField('大图')
    outline = models.CharField('简述', max_length=1024)
    route = models.CharField('路线', max_length=64)
    planning = models.TextField('行程安排')
    fee_desc = models.TextField('费用说明')
    equipment = models.TextField('出行装备')
    equipments = models.ManyToManyField(Equipment, verbose_name='装备租赁')

    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    cre_user_id = models.IntegerField('创建用户ID')
    upd_time = models.DateTimeField('修改时间', auto_now=True)
    upd_user_id = models.IntegerField('修改用户ID')


class Session(models.Model):
    event = models.ForeignKey(Event, verbose_name='活动')
    start_dt = models.DateField('开始日期')
    num_apply = models.IntegerField('已经报名人数', default=0)
    auto = models.BooleanField('报名自动通过', default=False)

    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('修改时间', auto_now=True)
