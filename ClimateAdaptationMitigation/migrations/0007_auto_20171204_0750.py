# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClimateAdaptationMitigation', '0006_auto_20171116_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edges',
            name='weight',
        ),
        migrations.AddField(
            model_name='entity',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
