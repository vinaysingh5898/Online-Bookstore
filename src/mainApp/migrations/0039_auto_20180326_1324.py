# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0038_adminrecommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminrecommendation',
            name='RecommendedBy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
