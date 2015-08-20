# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_equipment_equipmentgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='equipments',
            field=models.ManyToManyField(to='event.Equipment', verbose_name=b'\xe8\xa3\x85\xe5\xa4\x87\xe7\xa7\x9f\xe8\xb5\x81'),
        ),
    ]
