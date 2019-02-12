# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0032_auto_20180318_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='DateOfPurchase1',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 18, 17, 57, 29, 216670, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
