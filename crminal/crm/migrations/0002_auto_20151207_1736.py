# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opportunitystage',
            old_name='timestamp',
            new_name='time_stamp',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='source',
            field=models.ForeignKey(help_text=b'How did this contact find out about this?', to='crm.Campaign'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='value',
            field=models.DecimalField(help_text=b'How much this opportunity is worth to the organization', max_digits=10, decimal_places=2),
        ),
    ]
