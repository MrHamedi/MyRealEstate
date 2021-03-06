from django import forms 
from .models import apartment,field
import math

class field_form(forms.ModelForm):
	class Meta:
		model=field
		fields=("name","adress","phone","email","area","price","meterPrice","image1","image2","image3","image4","document","title","description","tags"
			,"length","width","build_sides","front_progress","back_progress","max_allowed_floors")
		widgets={
			"estate_slug":forms.HiddenInput,
			"name":forms.HiddenInput,
		}
		fieldsete=(
			(None,{"fields":("adress","title","description")})
		)
class apartment_form(forms.ModelForm):
	class Meta:
		model=apartment
		fields=("name","adress","phone","email","area","price","meterPrice","image1","image2","image3","image4","document","title","description","tags","renter","renter_phone","floor","floors","floor_material","cabinet","phone","parking","rooms","status","heating_system","cooler","trade_type")
		widgets={
			"estate_slug":forms.HiddenInput,
			"name":forms.HiddenInput,
		}

class apartment_home_page_form(forms.Form):
	max_price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"home_page_form"}),required=False)
	min_price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"home_page_form"}),required=False)
	max_area=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"home_page_form"}),required=False)
	min_area=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"home_page_form"}),required=False)
	apartment=forms.BooleanField(widget=forms.HiddenInput,initial=True,required=False)

class field_home_page_form(forms.Form):
	max_price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"home_page_form"}),required=False)
	min_price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"home_page_form"}),required=False)
	max_area=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"home_page_form"}),required=False)
	min_area=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"home_page_form"}),required=False)
	field=forms.BooleanField(widget=forms.HiddenInput,initial=True,required=False)
