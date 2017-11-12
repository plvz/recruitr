# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_event_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='target_email1',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
