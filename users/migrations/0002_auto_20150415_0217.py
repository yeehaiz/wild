# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='used_time',
            field=models.DateTimeField(null=True, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='user_id',
            field=models.IntegerField(null=True, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe8\x80\x85ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5'),
        ),
    ]
