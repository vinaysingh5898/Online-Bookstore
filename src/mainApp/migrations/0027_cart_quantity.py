# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0026_remove_cart_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(null=True, blank=True, default=0),
        ),
    ]
