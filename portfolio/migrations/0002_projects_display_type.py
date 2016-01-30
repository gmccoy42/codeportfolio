# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='display_type',
            field=models.CharField(default=datetime.datetime(2016, 1, 23, 22, 38, 52, 192475, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
