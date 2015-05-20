from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

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

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	rumuz = models.CharField(max_length = 15, unique=True)
	bitirilen_is_puani = models.IntegerField(default=0)
	teslim_edilmeyen_is = models.IntegerField(default=0)
	yaptirilan_is_puani = models.IntegerField(default=0)
	teslim_alinmayan_is = models.IntegerField(default=0)
	status = models.IntegerField(choices=((1, "Aktif"), 
		(2, "Pasif")),
	default = 1)

	def __unicode__(self):
		return self.user.username

class Is(models.Model):
	tanim = models.CharField(max_length=140)
	baslangic_tarihi = models.DateTimeField(default = datetime.now)
	bitis_tarihi = models.DateTimeField()
	detay = models.CharField(max_length=140)
	#TODO etiketler = models.ManyToManyField(Etiket)
	sehir = models.ForeignKey(Sehir, blank=True, null=True)
	olusturan_kullanici = models.ForeignKey(User, related_name="olusturan_kullanici")
	isi_yapan_kullanici = models.ForeignKey(User, related_name="isi_yapan_kullanici", null=True)
	teslim_edildi = models.BooleanField(default=False)
	status = models.IntegerField(choices=((1, "Henuz yapilmadi"), 
		(2, "Yapiliyor"), 
		(3, "Yapildi"), 
		(4, "Onaylandi")),
	default = 1)

	def __unicode__(self):
		return self.tanim

class Document(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	isid = models.ForeignKey(Is)