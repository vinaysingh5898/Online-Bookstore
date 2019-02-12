# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0027_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Quantity',
            field=models.IntegerField(default=0, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ProfileImg',
            field=models.ImageField(default='img/CustomerPic/no-img.jpg', upload_to='img/CustomerPic/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='DateOfDelivary',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='DateOfShipment',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
