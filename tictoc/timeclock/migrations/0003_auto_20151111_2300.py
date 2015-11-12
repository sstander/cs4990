# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeclock', '0002_auto_20151028_1921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='punch',
            options={'ordering': ('-time_in',), 'verbose_name_plural': 'punches'},
        ),
    ]
