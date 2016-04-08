# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_stockrecord_henk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockrecord',
            name='partner_sku',
            field=models.CharField(max_length=1280, verbose_name=b'Partner SKU'),
        ),
    ]
