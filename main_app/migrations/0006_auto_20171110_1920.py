# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_applicant_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='applicant_positions',
            field=models.ManyToManyField(default=1, to='main_app.Employee'),
        ),
    ]
