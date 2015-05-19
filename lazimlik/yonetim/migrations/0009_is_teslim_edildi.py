# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0008_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='is',
            name='teslim_edildi',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
