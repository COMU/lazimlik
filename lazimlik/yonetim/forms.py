from django import forms

from .models import yapilacakIs

class yapilacakIsForm(forms.ModelForm):
	class Meta:
		model = yapilacakIs