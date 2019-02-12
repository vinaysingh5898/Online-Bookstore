# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0029_auto_20180318_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Title',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
