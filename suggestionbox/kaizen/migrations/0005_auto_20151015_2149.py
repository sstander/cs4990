# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaizen', '0004_auto_20151015_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='person',
            field=models.CharField(max_length=200),
        ),
    ]
