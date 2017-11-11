# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20171110_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='applicant_positions',
            field=models.ManyToManyField(to='main_app.Position'),
        ),
    ]
