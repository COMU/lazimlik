# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='isAlan',
            fields=[
                ('isAlanId', models.AutoField(serialize=False, primary_key=True)),
                ('rumuz', models.CharField(max_length=40)),
                ('bitirilenIsPuani', models.IntegerField()),
                ('teslimEdilmeyenIs', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='isVeren',
            fields=[
                ('isVerenId', models.AutoField(serialize=False, primary_key=True)),
                ('rumuz', models.CharField(max_length=40)),
                ('yaptirilanIsPuani', models.IntegerField()),
                ('teslimAlinmayanIs', models.IntegerField()),
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
            model_name='isveren',
            name='isler',
            field=models.ManyToManyField(to='yonetim.yapilacakIs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='isalan',
            name='isler',
            field=models.ManyToManyField(to='yonetim.yapilacakIs'),
            preserve_default=True,
        ),
    ]
