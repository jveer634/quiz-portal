from django import forms
from accounts.models import User

class UserCreationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class UserChangeForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name', 'email', 'regdno']