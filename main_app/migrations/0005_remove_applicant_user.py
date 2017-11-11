# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_applicant_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='user',
        ),
    ]
