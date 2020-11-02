from django import forms

class contactUs_form(forms.Form):
	name=forms.CharField(max_length=200)
	advice=forms.CharField(widget=forms.Textarea)
	email=forms.EmailField()
	username=forms.CharField(widget=forms.HiddenInput,required=False)