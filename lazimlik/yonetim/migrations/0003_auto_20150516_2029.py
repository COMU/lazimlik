# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yonetim', '0002_auto_20150513_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Is',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tanim', models.CharField(max_length=140)),
                ('baslangic_tarihi', models.DateTimeField(auto_now_add=True)),
                ('bitis_tarihi', models.DateTimeField()),
                ('detay', models.CharField(max_length=140)),
                ('etiketler', models.ManyToManyField(to='yonetim.Etiket')),
                ('isi_yapan_kullanici', models.ForeignKey(related_name='isi_yapan_kullanici', to=settings.AUTH_USER_MODEL)),
                ('olusturan_kullanici', models.ForeignKey(related_name='olusturan_kullanici', to=settings.AUTH_USER_MODEL)),
                ('sehir', models.ForeignKey(to='yonetim.Sehir')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='verilenis',
            name='etiketler',
        ),
        migrations.RemoveField(
            model_name='verilenis',
            name='sehir',
        ),
        migrations.RemoveField(
            model_name='yapilacakis',
            name='etiketler',
        ),
        migrations.RemoveField(
            model_name='yapilacakis',
            name='sehir',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='aldigi_isler',
        ),
        migrations.DeleteModel(
            name='YapilacakIs',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='verdigi_isler',
        ),
        migrations.DeleteModel(
            name='VerilenIs',
        ),
    ]
