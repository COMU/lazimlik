from django import forms

from .models import YapilacakIs
from .models import UserProfile

class YapilacakIsForm(forms.ModelForm):
	class Meta:
		model = YapilacakIs

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		widgets={
			'user':forms.HiddenInput(),
		}