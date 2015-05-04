# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_verifycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='ip',
            field=models.GenericIPAddressField(verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
