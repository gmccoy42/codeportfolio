# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_projects_display_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='langauge',
            new_name='language',
        ),
    ]
