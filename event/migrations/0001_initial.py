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
                ('start_dt', models.DateField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f')),
                ('end_dt', models.DateField(verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('num_min', models.IntegerField(verbose_name=b'\xe6\x9c\x80\xe5\xb0\x91\xe4\xba\xba\xe6\x95\xb0')),
                ('num_max', models.IntegerField(verbose_name=b'\xe6\x9c\x80\xe5\xa4\x9a\xe4\xba\xba\xe6\x95\xb0')),
                ('price', models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=8, decimal_places=2)),
                ('outline', models.CharField(max_length=256, verbose_name=b'\xe7\xae\x80\xe8\xbf\xb0')),
                ('route', models.CharField(max_length=32, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf')),
                ('overview', models.TextField(verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf\xe6\xa6\x82\xe8\xbf\xb0')),
                ('planning', models.TextField(verbose_name=b'\xe8\xa1\x8c\xe7\xa8\x8b\xe5\xae\x89\xe6\x8e\x92')),
                ('notice', models.TextField(verbose_name=b'\xe6\xb3\xa8\xe6\x84\x8f\xe4\xba\x8b\xe9\xa1\xb9')),
                ('fee_desc', models.TextField(verbose_name=b'\xe8\xb4\xb9\xe7\x94\xa8\xe8\xaf\xb4\xe6\x98\x8e')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('cre_user', models.CharField(max_length=32, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x94\xa8\xe6\x88\xb7')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_user', models.CharField(max_length=32, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe7\x94\xa8\xe6\x88\xb7')),
            ],
        ),
        migrations.CreateModel(
            name='EventTheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('is_active', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('is_active', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='theme',
            field=models.ForeignKey(to='event.EventTheme'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(to='event.EventType'),
        ),
    ]
