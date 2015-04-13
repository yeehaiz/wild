# coding: utf-8

from django.db import models


class EventType(models.Model):
    name = models.CharField('类型名称', max_length=16)
    sort = models.IntegerField('排序')
    is_active = models.BooleanField('是否有效')

    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('修改时间', auto_now=True)



class EventTheme(models.Model):
    name = models.CharField('主题名称', max_length=16)
    sort = models.IntegerField('排序')
    is_active = models.BooleanField('是否有效')

    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('修改时间', auto_now=True)



class Event(models.Model):
    title = models.CharField('标题', max_length=64)
    theme = models.ForeignKey(EventTheme, verbose_name='活动主题')
    type = models.ForeignKey(EventType, verbose_name='活动类型')
    intensity = models.IntegerField('活动强度')
    days = models.IntegerField('活动天数')
    places = models.IntegerField('名额')
    price = models.DecimalField('价格', max_digits=9, decimal_places=2)

    outline = models.CharField('简述', max_length=256)
    route = models.CharField('路线', max_length=32)
    overview = models.TextField('路线概述')
    planning = models.TextField('行程安排')
    notice = models.TextField('注意事项')
    fee_desc = models.TextField('费用说明')

    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    cre_user = models.CharField('创建用户', max_length=32)
    upd_time = models.DateTimeField('修改时间', auto_now=True)
    upd_user = models.CharField('修改用户', max_length=32)


class Session(models.Model):
    event = models.ForeignKey(Event, verbose_name='活动')
    start_dt = models.DateField('开始日期')
    num_apply = models.IntegerField('已经报名人数')

    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('修改时间', auto_now=True)
