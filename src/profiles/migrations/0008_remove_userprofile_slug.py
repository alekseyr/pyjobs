# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_userprofile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='slug',
        ),
    ]