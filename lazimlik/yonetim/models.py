from django.db import models
from django.contrib.auth.models import User

class sehir(models.Model):
	sehirId = models.AutoField(primary_key = True)
	sehirAdi = models.CharField(max_length = 40)

	def __unicode__(self):
		return self.sehirAdi

class etiket(models.Model):
	etiketId = models.AutoField(primary_key = True)
	etiketAdi = models.CharField(max_length = 40)

	def __unicode__(self):
		return self.etiketAdi

class yapilacakIs(models.Model):
	isId = models.AutoField(primary_key = True)
	tanimi = models.CharField(max_length = 140)
	baslamaTarihi = models.DateTimeField()
	bitisTarihi = models.DateTimeField()
	detaylar = models.CharField(max_length = 140)
	etiketler = models.ManyToManyField(etiket)     
	sehir = models.ForeignKey(sehir)

	def __unicode__(self):
		return self.tanimi

class kullanici(models.Model):
	user = models.ForeignKey(User)
	bitirilenIsPuani = models.IntegerField(default=0)
	teslimEdilmeyenIs = models.IntegerField(default=0)
	isler = models.ManyToManyField(yapilacakIs, blank=True)
	yaptirilanIsPuani = models.IntegerField(default=0)
	teslimAlinmayanIs = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user.username