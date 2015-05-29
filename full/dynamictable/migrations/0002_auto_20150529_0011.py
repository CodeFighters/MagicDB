# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamictable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='tname',
            field=models.TextField(null=True, unique=True, blank=True),
        ),
    ]
