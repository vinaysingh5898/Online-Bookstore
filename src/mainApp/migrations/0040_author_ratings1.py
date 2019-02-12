# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0039_auto_20180326_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='Ratings1',
            field=models.IntegerField(default=0),
        ),
    ]
