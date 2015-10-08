# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import userena.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kaizen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('view_profile', 'Can view profile'),)},
        ),
        migrations.AddField(
            model_name='profile',
            name='mugshot',
            field=easy_thumbnails.fields.ThumbnailerImageField(help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='privacy',
            field=models.CharField(default=b'registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy', choices=[(b'open', 'Open'), (b'registered', 'Registered'), (b'closed', 'Closed')]),
        ),
    ]
