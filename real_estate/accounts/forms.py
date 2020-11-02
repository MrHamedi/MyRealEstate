from django import forms 
from .models import profile
from django.contrib.auth.models import User

class profile_form(forms.ModelForm):
	class Meta:
		model=profile
		fields=("name","family","image","phone","email")
class register_form(forms.ModelForm):
	password=forms.CharField()
	password2=forms.CharField(label="Enter your password again")
	class Meta:
		model=User
		fields=("username",)
	def clean_password2(self):
		form=self.cleaned_data
		if(form["password"]==form["password2"]):
			return(form["password2"])
		else:
			raise(forms.ValidationError("The passwords does not match"))
