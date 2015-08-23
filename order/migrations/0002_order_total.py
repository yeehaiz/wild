# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(default=0, verbose_name=b'\xe6\x80\xbb\xe9\x87\x91\xe9\xa2\x9d', max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
    ]
