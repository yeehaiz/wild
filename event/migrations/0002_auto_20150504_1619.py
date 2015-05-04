# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        migrations.AddField(
            model_name='event',
            name='type_id',
            field=models.IntegerField(default=2, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe7\xb1\xbb\xe5\x9e\x8b'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='num_apply',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xb7\xb2\xe7\xbb\x8f\xe6\x8a\xa5\xe5\x90\x8d\xe4\xba\xba\xe6\x95\xb0'),
        ),
        migrations.DeleteModel(
            name='EventType',
        ),
    ]
