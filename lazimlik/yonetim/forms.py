from django import forms

from models import Is
from models import UserProfile

class IsForm(forms.ModelForm):
	class Meta:
		model = Is
		fields = '__all__'
		exclude = ['olusturan_kullanici', 'isi_yapan_kullanici']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		widgets={
			'user':forms.HiddenInput(),
		}
		fields = '__all__'

class DocumentForm(forms.Form):
	docfile = forms.FileField(
		label='Select a file'
	)