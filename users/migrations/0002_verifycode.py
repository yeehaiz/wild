# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=16, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
                ('vcode', models.IntegerField(verbose_name=b'\xe9\xaa\x8c\xe8\xaf\x81\xe7\xa0\x81')),
                ('ip', models.IPAddressField(verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80')),
                ('vtimes', models.IntegerField(verbose_name=b'\xe9\xaa\x8c\xe8\xaf\x81\xe9\x94\x99\xe8\xaf\xaf\xe6\xac\xa1\xe6\x95\xb0')),
                ('cre_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
