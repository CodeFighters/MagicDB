# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0003_auto_20150528_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='season',
            field=models.TextField(null=True, blank=True),
        ),
    ]
