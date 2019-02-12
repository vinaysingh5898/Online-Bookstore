# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0024_auto_20180317_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Content',
            field=models.TextField(blank=True, null=True, max_length=500),
        ),
    ]
