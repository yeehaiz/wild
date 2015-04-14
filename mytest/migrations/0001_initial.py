# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('y', models.CharField(max_length=20)),
                ('z', models.ForeignKey(to='mytest.A')),
            ],
        ),
    ]
