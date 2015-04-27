# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('intensity', models.IntegerField(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\xbc\xba\xe5\xba\xa6')),
                ('days', models.IntegerField(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\xa4\xa9\xe6\x95\xb0')),
                ('places', models.IntegerField(verbose_name=b'\xe5\x90\x8d\xe9\xa2\x9d')),
                ('price', models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=9, decimal_places=2)),
                ('covers', models.TextField(verbose_name=b'\xe5\xa4\xa7\xe5\x9b\xbe')),
                ('outline', models.CharField(max_length=1024, verbose_name=b'\xe7\xae\x80\xe8\xbf\xb0')),
                ('route', models.CharField(max_length=64, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf')),
                ('planning', models.TextField(verbose_name=b'\xe8\xa1\x8c\xe7\xa8\x8b\xe5\xae\x89\xe6\x8e\x92')),
                ('fee_desc', models.TextField(verbose_name=b'\xe8\xb4\xb9\xe7\x94\xa8\xe8\xaf\xb4\xe6\x98\x8e')),
                ('equipment', models.TextField(verbose_name=b'\xe5\x87\xba\xe8\xa1\x8c\xe8\xa3\x85\xe5\xa4\x87')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('cre_user', models.CharField(max_length=32, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x94\xa8\xe6\x88\xb7')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_user', models.CharField(max_length=32, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe7\x94\xa8\xe6\x88\xb7')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_dt', models.DateField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f')),
                ('num_apply', models.IntegerField(verbose_name=b'\xe5\xb7\xb2\xe7\xbb\x8f\xe6\x8a\xa5\xe5\x90\x8d\xe4\xba\xba\xe6\x95\xb0')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('event', models.ForeignKey(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8', to='event.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe7\xb1\xbb\xe5\x9e\x8b', to='event.EventType'),
        ),
    ]
