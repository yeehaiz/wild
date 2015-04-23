# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150423_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='outline',
            field=models.CharField(max_length=1024, verbose_name=b'\xe7\xae\x80\xe8\xbf\xb0'),
        ),
    ]
