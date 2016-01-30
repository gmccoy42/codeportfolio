# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20160123_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='language',
            field=models.CharField(max_length=200),
        ),
    ]
