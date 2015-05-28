# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groceries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.SmallIntegerField()),
                ('measurement', models.CharField(max_length=20)),
                ('is_bought', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
