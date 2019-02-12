# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0040_author_ratings1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='Ratings1',
        ),
    ]
