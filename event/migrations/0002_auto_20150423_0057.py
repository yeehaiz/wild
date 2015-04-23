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
            name='notice',
        ),
        migrations.RemoveField(
            model_name='event',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='event',
            name='theme',
        ),
        migrations.AddField(
            model_name='event',
            name='equipment',
            field=models.TextField(default='', verbose_name=b'\xe5\x87\xba\xe8\xa1\x8c\xe8\xa3\x85\xe5\xa4\x87'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='route',
            field=models.CharField(max_length=64, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88'),
        ),
        migrations.DeleteModel(
            name='EventTheme',
        ),
    ]
