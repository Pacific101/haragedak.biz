# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-06-28 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_restraunt_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='restraunt',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='main_app/'),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='main_app/'),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='main_app/'),
        ),
    ]
