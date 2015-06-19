# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_equipment_equipmentgroup'),
        ('users', '0005_frequentmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name=b'\xe4\xba\xba\xe6\x95\xb0')),
                ('contact_name', models.CharField(max_length=16, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('contact_mobile', models.CharField(max_length=16, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe6\x89\x8b\xe6\x9c\xba')),
                ('comment', models.CharField(max_length=512, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
                ('apply_fee', models.DecimalField(verbose_name=b'\xe6\x8a\xa5\xe5\x90\x8d\xe8\xb4\xb9', max_digits=9, decimal_places=2)),
                ('equipment_rent', models.DecimalField(verbose_name=b'\xe8\xa3\x85\xe5\xa4\x87\xe7\xa7\x9f\xe9\x87\x91', max_digits=9, decimal_places=2)),
                ('equipment_status', models.IntegerField(default=0, verbose_name=b'\xe8\xa3\x85\xe5\xa4\x87\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\xbe\x85\xe5\x8f\x96'), (1, b'\xe5\x80\x9f\xe5\x87\xba'), (2, b'\xe5\xae\x8c\xe6\x88\x90')])),
                ('status', models.IntegerField(default=0, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\xbe\x85\xe6\x94\xaf\xe4\xbb\x98'), (1, b'\xe5\xb7\xb2\xe6\x94\xaf\xe4\xbb\x98'), (-1, b'\xe5\xb7\xb2\xe5\x8f\x96\xe6\xb6\x88'), (-2, b'\xe5\xb7\xb2\xe9\x80\x80\xe6\xac\xbe')])),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('session', models.ForeignKey(verbose_name=b'\xe5\x9c\xba\xe6\xac\xa1', to='event.Session')),
                ('user', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderEquipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('equipment', models.ForeignKey(verbose_name=b'\xe8\xa3\x85\xe5\xa4\x87', to='event.Equipment')),
                ('order', models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95', to='order.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('mobile', models.CharField(max_length=16, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
                ('cert_type', models.IntegerField(verbose_name=b'\xe8\xaf\x81\xe4\xbb\xb6\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81'), (2, b'\xe6\x8a\xa4\xe7\x85\xa7'), (3, b'\xe5\x86\x9b\xe5\xae\x98\xe8\xaf\x81'), (4, b'\xe5\x9b\x9e\xe4\xb9\xa1\xe8\xaf\x81')])),
                ('cert', models.CharField(max_length=32, verbose_name=b'\xe8\xaf\x81\xe4\xbb\xb6\xe5\x8f\xb7')),
                ('sex', models.CharField(max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'm', b'\xe7\x94\xb7'), (b'f', b'\xe5\xa5\xb3')])),
                ('birthday', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5')),
                ('order', models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95', to='order.Order')),
            ],
        ),
    ]
