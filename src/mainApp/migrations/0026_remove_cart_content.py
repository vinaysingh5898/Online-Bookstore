# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0025_cart_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Content',
        ),
    ]
