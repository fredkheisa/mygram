# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-11 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_picture_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='location',
            new_name='category',
        ),
    ]
