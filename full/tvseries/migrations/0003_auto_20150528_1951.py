# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0002_auto_20150527_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='user_id',
            new_name='user',
        ),
    ]
