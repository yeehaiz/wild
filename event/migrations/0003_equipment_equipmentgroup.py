# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150504_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe8\xa3\x85\xe5\xa4\x87\xe5\x90\x8d')),
                ('rent', models.DecimalField(verbose_name=b'\xe7\xa7\x9f\xe9\x87\x91', max_digits=9, decimal_places=2)),
                ('price', models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=9, decimal_places=2)),
                ('storage', models.IntegerField(verbose_name=b'\xe5\xba\x93\xe5\xad\x98\xe6\x95\xb0\xe9\x87\x8f')),
                ('num_out', models.IntegerField(verbose_name=b'\xe5\x80\x9f\xe5\x87\xba\xe6\x95\xb0\xe9\x87\x8f')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'\xe7\xbb\x84\xe5\x90\x88\xe5\x90\x8d')),
                ('discount', models.DecimalField(verbose_name=b'\xe6\x8a\x98\xe6\x89\xa3', max_digits=2, decimal_places=1)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('equipments', models.ManyToManyField(to='event.Equipment', verbose_name=b'\xe8\xa3\x85\xe5\xa4\x87\xe4\xbb\xac')),
            ],
        ),
    ]
