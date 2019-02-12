# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0023_remove_review_contents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Book', models.ForeignKey(to='mainApp.BookEdition')),
                ('Customer', models.ForeignKey(to='mainApp.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='kart',
            name='Book',
        ),
        migrations.RemoveField(
            model_name='kart',
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Kart',
        ),
    ]
