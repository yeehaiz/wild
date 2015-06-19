# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150505_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('mobile', models.CharField(max_length=16, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
                ('cert_type', models.IntegerField(verbose_name=b'\xe8\xaf\x81\xe4\xbb\xb6\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81'), (2, b'\xe6\x8a\xa4\xe7\x85\xa7'), (3, b'\xe5\x86\x9b\xe5\xae\x98\xe8\xaf\x81'), (4, b'\xe5\x9b\x9e\xe4\xb9\xa1\xe8\xaf\x81')])),
                ('cert', models.CharField(max_length=32, verbose_name=b'\xe8\xaf\x81\xe4\xbb\xb6\xe5\x8f\xb7')),
                ('sex', models.CharField(max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'm', b'\xe7\x94\xb7'), (b'f', b'\xe5\xa5\xb3')])),
                ('birthday', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5')),
                ('user', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='users.User')),
            ],
        ),
    ]
