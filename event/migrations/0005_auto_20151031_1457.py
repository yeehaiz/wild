# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_equipments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentgroup',
            name='equipments',
        ),
        migrations.AddField(
            model_name='session',
            name='auto',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x8a\xa5\xe5\x90\x8d\xe8\x87\xaa\xe5\x8a\xa8\xe9\x80\x9a\xe8\xbf\x87'),
        ),
        migrations.DeleteModel(
            name='EquipmentGroup',
        ),
    ]
