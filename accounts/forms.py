from django import forms

from accounts.models import Staff, Student

class StaffCreationForm(forms.ModelForm):
	class Meta:
		model = Staff
		fields = '__all__'

class StaffChangeForm(forms.ModelForm):
	class Meta:
		model = Staff
		fields = '__all__'