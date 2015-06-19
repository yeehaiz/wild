# coding: utf-8

from django.db import models


class User(models.Model):
    SEX_CHOICES = (('m', '男'), ('f', '女'), ('u', '未知'))

    username = models.CharField('用户名', max_length=32, unique=True)
    mobile = models.CharField('注册手机', max_length=16, unique=True)
    password = models.CharField('密码', max_length=32)

    nickname = models.CharField('昵称', max_length=16, default='')
    avatar = models.CharField('头像地址', max_length=256, default='')
    sex = models.CharField('性别', max_length=1, choices=SEX_CHOICES, default='u')
    birthday = models.DateField('生日', null=True)

    balance = models.DecimalField('余额', max_digits=9, decimal_places=2, default=0)
    level = models.IntegerField('会员等级', default=0)

    is_active = models.BooleanField('是否有效', default=True)
    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('更新时间', auto_now=True)


class Admin(models.Model):
    user_id = models.IntegerField('用户ID', primary_key = True)
    level = models.IntegerField('管理员等级')
    is_super = models.BooleanField('是否拥有超级权限', default = False)

    cre_user_id = models.IntegerField('创建者ID')
    upd_user_id = models.IntegerField('更新者ID')
    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('更新时间', auto_now=True)


class Coupon(models.Model):
    amount = models.DecimalField('金额', max_digits=9, decimal_places=2)
    exch_code = models.CharField('对换码', max_length=16)

    used = models.BooleanField('已使用', default=False)
    user_id = models.IntegerField('使用者ID', null=True)
    used_time = models.DateTimeField('使用时间', null=True)

    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('更新时间', auto_now=True)


class VerifyCode(models.Model):
    mobile = models.CharField('手机', max_length=16)
    vcode = models.IntegerField('验证码')
    ip = models.GenericIPAddressField('IP地址')
    vtimes = models.IntegerField('验证错误次数', default=0)
    cre_time = models.DateTimeField('创建时间', auto_now_add=True)
    upd_time = models.DateTimeField('更新时间', auto_now=True)


class FrequentMember(models.Model):
    CERT_TYPES = ((1, '身份证'), (2, '护照'), (3, '军官证'), (4, '回乡证'))
    SEX_CHOICES = (('m', '男'), ('f', '女'))

    user = models.ForeignKey(User, verbose_name='用户')
    name = models.CharField('姓名', max_length=16)
    mobile = models.CharField('手机', max_length=16)
    cert_type = models.IntegerField('证件类型', choices=CERT_TYPES)
    cert = models.CharField('证件号', max_length=32)
    sex = models.CharField('性别', max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField('生日')
