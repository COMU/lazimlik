# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0003_auto_20150516_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='is',
            name='etiketler',
        ),
        migrations.AlterField(
            model_name='is',
            name='baslangic_tarihi',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
