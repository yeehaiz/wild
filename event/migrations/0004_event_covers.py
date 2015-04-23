# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20150423_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='covers',
            field=models.TextField(default='', verbose_name=b'\xe5\xa4\xa7\xe5\x9b\xbe'),
            preserve_default=False,
        ),
    ]
