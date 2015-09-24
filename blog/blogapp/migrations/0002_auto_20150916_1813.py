# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=0, to='blogapp.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blogapp.Category', null=True, blank=True),
        ),
    ]
