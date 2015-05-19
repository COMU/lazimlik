# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0009_is_teslim_edildi'),
    ]

    operations = [
        migrations.AddField(
            model_name='is',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Henuz yapilmadi'), (2, b'Yapiliyor'), (3, b'Yapildi'), (4, b'Onaylandi')]),
            preserve_default=True,
        ),
    ]
