# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0004_auto_20150516_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='is',
            name='sehir',
            field=models.ForeignKey(to='yonetim.Sehir', blank=True),
            preserve_default=True,
        ),
    ]
