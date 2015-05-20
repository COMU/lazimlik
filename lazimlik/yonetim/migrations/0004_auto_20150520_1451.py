# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0003_auto_20150520_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='is',
            name='isi_yapan_kullanici',
            field=models.ForeignKey(related_name='isi_yapan_kullanici', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='is',
            name='olusturan_kullanici',
            field=models.ForeignKey(related_name='olusturan_kullanici', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
