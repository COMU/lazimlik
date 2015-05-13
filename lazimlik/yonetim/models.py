from django.db import models
from django.contrib.auth.models import User

class Sehir(models.Model):
	sehir_id = models.AutoField(primary_key = True)
	sehir_adi = models.CharField(max_length = 40)

	def __unicode__(self):
		return self.sehir_adi

class Etiket(models.Model):
	etiket_id = models.AutoField(primary_key = True)
	etiket_adi = models.CharField(max_length = 40)

	def __unicode__(self):
		return self.etiket_adi

class YapilacakIs(models.Model):
	is_id = models.AutoField(primary_key = True)
	tanimi = models.CharField(max_length = 140)
	baslama_tarihi = models.DateTimeField()
	bitis_tarihi = models.DateTimeField()
	detaylar = models.CharField(max_length = 140)
	etiketler = models.ManyToManyField(Etiket)     
	sehir = models.ForeignKey(Sehir)

	def __unicode__(self):
		return self.tanimi

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	rumuz = models.CharField(max_length = 15, unique=True)
	bitirilen_is_puani = models.IntegerField(default=0)
	teslim_edilmeyen_is = models.IntegerField(default=0)
	isler = models.ManyToManyField(YapilacakIs, blank=True)
	yaptirilan_is_puani = models.IntegerField(default=0)
	teslim_alinmayan_is = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user.username