# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClimateAdaptationMitigation', '0002_auto_20171029_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='abbreviation',
            new_name='abbr',
        ),
    ]
