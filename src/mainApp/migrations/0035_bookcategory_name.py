# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0034_remove_order_dateofpurchase1'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcategory',
            name='Name',
            field=models.CharField(max_length=120, default=datetime.datetime(2018, 3, 18, 19, 46, 18, 135414, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
