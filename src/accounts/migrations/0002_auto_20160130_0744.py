# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recruiter',
            field=models.BooleanField(default=False, verbose_name='Ищу работников'),
        ),
        migrations.AddField(
            model_name='user',
            name='worker',
            field=models.BooleanField(default=False, verbose_name='Ищу работу'),
        ),
    ]