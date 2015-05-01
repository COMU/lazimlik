from django import forms

from .models import yapilacakIs
from .models import kullanici

class yapilacakIsForm(forms.ModelForm):
	class Meta:
		model = yapilacakIs

class kullaniciForm(forms.ModelForm):
	class Meta:
		model = kullanici