# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_event_target_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='schedule',
            field=models.TimeField(default=datetime.datetime(2017, 11, 11, 18, 38, 4, 464206, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
