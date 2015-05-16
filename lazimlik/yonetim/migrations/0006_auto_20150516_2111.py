# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0005_auto_20150516_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='is',
            name='sehir',
            field=models.ForeignKey(blank=True, to='yonetim.Sehir', null=True),
            preserve_default=True,
        ),
    ]
