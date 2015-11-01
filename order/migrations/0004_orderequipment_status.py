# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20151031_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderequipment',
            name='status',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xa3\x85\xe5\xa4\x87\xe7\xa7\x9f\xe8\xb5\x81\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\xad\xa3\xe5\xb8\xb8'), (-1, b'\xe5\x8f\x96\xe6\xb6\x88')]),
        ),
    ]
