# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='query',
        ),
    ]
