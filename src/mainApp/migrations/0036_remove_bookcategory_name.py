# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0035_bookcategory_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategory',
            name='Name',
        ),
    ]
