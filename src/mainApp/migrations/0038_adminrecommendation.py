# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0037_book_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminRecommendation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('RecommendedBy', models.ForeignKey(to='mainApp.Admin')),
            ],
        ),
    ]
