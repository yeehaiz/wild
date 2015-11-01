# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderequipment',
            name='end_dt',
            field=models.DateField(default=datetime.datetime(2015, 10, 31, 14, 57, 54, 851396), verbose_name=b'\xe5\xbd\x92\xe8\xbf\x98\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderequipment',
            name='start_dt',
            field=models.DateField(default=datetime.datetime(2015, 10, 31, 14, 57, 58, 913142), verbose_name=b'\xe5\x87\xba\xe5\x80\x9f\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe6\x9c\xaa\xe5\xae\xa1\xe6\xa0\xb8'), (2, b'\xe9\xa2\x84\xe5\xae\xa1\xe9\x80\x9a\xe8\xbf\x87'), (3, b'\xe5\xb7\xb2\xe9\x80\x9a\xe8\xbf\x87'), (4, b'\xe6\x8a\xa5\xe5\x90\x8d\xe6\x88\x90\xe5\x8a\x9f'), (5, b'\xe6\x9b\xbf\xe8\xa1\xa5'), (-1, b'\xe5\xb7\xb2\xe5\x8f\x96\xe6\xb6\x88'), (-2, b'\xe5\xb7\xb2\xe9\x80\x80\xe6\xac\xbe')]),
        ),
    ]
