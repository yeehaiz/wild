# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150504_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='vtimes',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\xaa\x8c\xe8\xaf\x81\xe9\x94\x99\xe8\xaf\xaf\xe6\xac\xa1\xe6\x95\xb0'),
        ),
    ]
