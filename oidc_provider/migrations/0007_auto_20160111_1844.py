# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 18:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0006_unique_user_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='code',
            options={'verbose_name': 'Authorization Code', 'verbose_name_plural': 'Authorization Codes'},
        ),
        migrations.AlterModelOptions(
            name='token',
            options={'verbose_name': 'Token', 'verbose_name_plural': 'Tokens'},
        ),
        migrations.AddField(
            model_name='client',
            name='date_created',
            field=models.DateField(
                auto_now_add=True, default=datetime.datetime(2016, 1, 11, 18, 44, 32, 192477, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='_redirect_uris',
            field=models.TextField(default=b'', help_text='Enter each URI on a new line.', verbose_name='Redirect URI'),
        ),
    ]
