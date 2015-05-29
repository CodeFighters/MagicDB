# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamictable', '0002_auto_20150529_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='tname',
            field=models.TextField(blank=True, null=True),
        ),
    ]
