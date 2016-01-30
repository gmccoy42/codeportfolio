# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('display_type', models.CharField(max_length=200)),
                ('util', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('langauge', models.ForeignKey(to='portfolio.language')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
