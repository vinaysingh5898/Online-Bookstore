# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0036_remove_bookcategory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Authors',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
