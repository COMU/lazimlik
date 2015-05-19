# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etiket',
            fields=[
                ('etiket_id', models.AutoField(serialize=False, primary_key=True)),
                ('etiket_adi', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Is',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tanim', models.CharField(max_length=140)),
                ('baslangic_tarihi', models.DateTimeField(default=datetime.datetime.now)),
                ('bitis_tarihi', models.DateTimeField()),
                ('detay', models.CharField(max_length=140)),
                ('teslim_edildi', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Henuz yapilmadi'), (2, b'Yapiliyor'), (3, b'Yapildi'), (4, b'Onaylandi')])),
                ('isi_yapan_kullanici', models.ForeignKey(related_name='isi_yapan_kullanici', to=settings.AUTH_USER_MODEL, null=True)),
                ('materyal', models.OneToOneField(to='yonetim.Document')),
                ('olusturan_kullanici', models.ForeignKey(related_name='olusturan_kullanici', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sehir',
            fields=[
                ('sehir_id', models.AutoField(serialize=False, primary_key=True)),
                ('sehir_adi', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rumuz', models.CharField(unique=True, max_length=15)),
                ('bitirilen_is_puani', models.IntegerField(default=0)),
                ('teslim_edilmeyen_is', models.IntegerField(default=0)),
                ('yaptirilan_is_puani', models.IntegerField(default=0)),
                ('teslim_alinmayan_is', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='is',
            name='sehir',
            field=models.ForeignKey(blank=True, to='yonetim.Sehir', null=True),
            preserve_default=True,
        ),
    ]
