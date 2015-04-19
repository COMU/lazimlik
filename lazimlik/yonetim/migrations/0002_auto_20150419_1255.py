# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kullanici',
            fields=[
                ('kullaniciId', models.AutoField(serialize=False, primary_key=True)),
                ('rumuz', models.CharField(max_length=40)),
                ('bitirilenIsPuani', models.IntegerField()),
                ('teslimEdilmeyenIs', models.IntegerField()),
                ('yaptirilanIsPuani', models.IntegerField()),
                ('teslimAlinmayanIs', models.IntegerField()),
                ('isler', models.ManyToManyField(to='yonetim.yapilacakIs', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='isalan',
            name='isler',
        ),
        migrations.DeleteModel(
            name='isAlan',
        ),
        migrations.RemoveField(
            model_name='isveren',
            name='isler',
        ),
        migrations.DeleteModel(
            name='isVeren',
        ),
    ]
