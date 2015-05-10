# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='etiket',
            fields=[
                ('etiketId', models.AutoField(serialize=False, primary_key=True)),
                ('etiketAdi', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='kullanici',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bitirilenIsPuani', models.IntegerField(default=0)),
                ('teslimEdilmeyenIs', models.IntegerField(default=0)),
                ('yaptirilanIsPuani', models.IntegerField(default=0)),
                ('teslimAlinmayanIs', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sehir',
            fields=[
                ('sehirId', models.AutoField(serialize=False, primary_key=True)),
                ('sehirAdi', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='yapilacakIs',
            fields=[
                ('isId', models.AutoField(serialize=False, primary_key=True)),
                ('tanimi', models.CharField(max_length=140)),
                ('baslamaTarihi', models.DateTimeField()),
                ('bitisTarihi', models.DateTimeField()),
                ('detaylar', models.CharField(max_length=140)),
                ('etiketler', models.ManyToManyField(to='yonetim.etiket')),
                ('sehir', models.ForeignKey(to='yonetim.sehir')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='kullanici',
            name='isler',
            field=models.ManyToManyField(to='yonetim.yapilacakIs', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kullanici',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
