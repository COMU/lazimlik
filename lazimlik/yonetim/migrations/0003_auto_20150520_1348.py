# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0002_userprofile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='is',
            name='isi_yapan_kullanici',
            field=models.ForeignKey(related_name='isi_yapan_kullanici', to='yonetim.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='is',
            name='olusturan_kullanici',
            field=models.ForeignKey(related_name='olusturan_kullanici', to='yonetim.UserProfile'),
            preserve_default=True,
        ),
    ]
