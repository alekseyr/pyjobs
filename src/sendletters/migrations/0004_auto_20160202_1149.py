# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendletters', '0003_auto_20160130_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptionsignup',
            old_name='recruiter',
            new_name='is_recruiter',
        ),
        migrations.RenameField(
            model_name='subscriptionsignup',
            old_name='worker',
            new_name='is_worker',
        ),
    ]