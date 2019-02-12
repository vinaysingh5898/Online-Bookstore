# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0021_auto_20180317_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Contents',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
