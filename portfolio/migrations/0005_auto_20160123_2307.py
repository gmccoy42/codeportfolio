# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0004_auto_20160123_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='user',
        ),
        migrations.AddField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
