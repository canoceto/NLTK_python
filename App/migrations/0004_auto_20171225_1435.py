# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_author_headshot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
    ]
