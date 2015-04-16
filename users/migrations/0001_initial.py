# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(verbose_name=b'\xe9\x87\x91\xe9\xa2\x9d', max_digits=9, decimal_places=2)),
                ('exch_code', models.CharField(max_length=16, verbose_name=b'\xe5\xaf\xb9\xe6\x8d\xa2\xe7\xa0\x81')),
                ('used', models.BooleanField(default=False, verbose_name=b'\xe5\xb7\xb2\xe4\xbd\xbf\xe7\x94\xa8')),
                ('user_id', models.IntegerField(verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe8\x80\x85ID', blank=True)),
                ('used_time', models.DateTimeField(verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('mobile', models.CharField(unique=True, max_length=16, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x89\x8b\xe6\x9c\xba')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('nickname', models.CharField(default=b'', max_length=16, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('avatar', models.CharField(default=b'', max_length=256, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f\xe5\x9c\xb0\xe5\x9d\x80')),
                ('sex', models.CharField(default=b'u', max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'm', b'\xe7\x94\xb7'), (b'f', b'\xe5\xa5\xb3'), (b'u', b'\xe6\x9c\xaa\xe7\x9f\xa5')])),
                ('birthday', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5', blank=True)),
                ('balance', models.DecimalField(default=0, verbose_name=b'\xe4\xbd\x99\xe9\xa2\x9d', max_digits=9, decimal_places=2)),
                ('level', models.IntegerField(default=0, verbose_name=b'\xe4\xbc\x9a\xe5\x91\x98\xe7\xad\x89\xe7\xba\xa7')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
