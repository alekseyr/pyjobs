# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendletters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionsignup',
            name='email',
            field=models.EmailField(max_length=120, null=True, verbose_name='электропочта'),
        ),
        migrations.AlterField(
            model_name='subscriptionsignup',
            name='full_name',
            field=models.CharField(default='', max_length=120, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='subscriptionsignup',
            name='recruiter',
            field=models.BooleanField(verbose_name='Ищу работников'),
        ),
        migrations.AlterField(
            model_name='subscriptionsignup',
            name='worker',
            field=models.BooleanField(verbose_name='Ищу работу'),
        ),
    ]