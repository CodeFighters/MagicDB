# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0002_auto_20150528_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='groceries',
            name='list_name',
            field=models.ForeignKey(to='db_app.Lists'),
        ),
    ]
