# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 22:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0060_auto_20160627_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='DOB',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 6, 26, 22, 12, 35, 443445, tzinfo=utc)),
        ),
    ]
