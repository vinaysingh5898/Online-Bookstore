# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0031_auto_20180318_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='Discount',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0, help_text='Discount should be between 0% to 100%'),
        ),
    ]
