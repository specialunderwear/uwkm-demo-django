# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_auto_20160107_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockrecord',
            name='henk',
            field=models.NullBooleanField(),
        ),
    ]
