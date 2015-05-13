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
                ('rumuz', models.CharField(max_length=15)),
                ('bitirilen_is_puani', models.IntegerField(default=0)),
                ('teslim_edilmeyen_is', models.IntegerField(default=0)),
                ('yaptirilan_is_puani', models.IntegerField(default=0)),
                ('teslim_alinmayan_is', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YapilacakIs',
            fields=[
                ('is_id', models.AutoField(serialize=False, primary_key=True)),
                ('tanimi', models.CharField(max_length=140)),
                ('baslama_tarihi', models.DateTimeField()),
                ('bitis_tarihi', models.DateTimeField()),
                ('detaylar', models.CharField(max_length=140)),
                ('etiketler', models.ManyToManyField(to='yonetim.Etiket')),
                ('sehir', models.ForeignKey(to='yonetim.Sehir')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='isler',
            field=models.ManyToManyField(to='yonetim.YapilacakIs', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
