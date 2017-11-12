# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='target_email',
            field=models.EmailField(default='email@mail.com', max_length=254),
            preserve_default=False,
        ),
    ]
