# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaizen', '0003_auto_20151015_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='idea',
            name='status',
            field=models.CharField(max_length=3, choices=[(b'new', b'New'), (b'den', b'Denied'), (b'rev', b'In Review'), (b'2do', b'To Do'), (b'imp', b'Implemented')]),
        ),
    ]
