# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=50)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.CharField(default=b'anonymous', max_length=50),
        ),
        migrations.AddField(
            model_name='topic',
            name='users',
            field=models.ManyToManyField(to='App.User'),
        ),
    ]
