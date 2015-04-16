from django.db import models

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

class isAlan(models.Model):
    isAlanId = models.AutoField(primary_key = True)
    rumuz = models.CharField(max_length = 40)
    bitirilenIsPuani = models.IntegerField()
    teslimEdilmeyenIs = models.IntegerField()
    isler = models.ManyToManyField(yapilacakIs, blank=True)

    def __unicode__(self):
        return self.rumuz

class isVeren(models.Model):
    isVerenId = models.AutoField(primary_key = True)
    rumuz = models.CharField(max_length = 40)
    yaptirilanIsPuani = models.IntegerField()
    teslimAlinmayanIs = models.IntegerField()
    isler = models.ManyToManyField(yapilacakIs, blank=True)

    def __unicode__(self):
        return self.rumuz
