# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Aktif'), (2, b'Pasif')]),
            preserve_default=True,
        ),
    ]
