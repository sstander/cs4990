# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaizen', '0002_auto_20151007_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='idea',
            name='status',
            field=models.CharField(max_length=3, choices=[(b'new', b'New'), (b'den', b'Denied'), (b'rev', b'In Review'), (b'2d0', b'To Do'), (b'doi', b'Doing'), (b'imp', b'Implemented')]),
        ),
    ]
