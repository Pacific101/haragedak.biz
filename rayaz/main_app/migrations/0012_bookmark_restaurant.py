# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-07-15 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20190715_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookmarkz', to='main_app.Restraunt'),
        ),
    ]
