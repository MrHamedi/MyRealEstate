from estate.models import field,apartment
from django.shortcuts import render,get_object_or_404
from itertools import chain
from django.db.models import Min
from django.http import Http404,HttpResponseRedirect
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import field_form,apartment_form,apartment_home_page_form,field_home_page_form
from django.utils import timezone
from datetime import datetime
import operator
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def homePage_view(request):
	if("apartment" in request.GET):
		models=apartment.objects.all()
		if("min_price" in request.GET):
			min_price=request.GET.get("min_price")
			models=models.filter(price__gt=min_price)	
		if("max_price" in request.GET):
			max_price=request.GET.get("max_price")
			models=models.filter(price__lte=max_price)
	
	elif("field" in request.GET):
		models=field.objects.all()
		if("min_price" in request.GET):
			min_price=request.GET.get("min_price")
			models=models.filter(price__gt=min_price)	
		if("max_price" in request.GET):
			max_price=request.GET.get("max_price")
			models=models.filter(price__lte=max_price)
	
	else:
		apartments=apartment.objects.all()
		fields=field.objects.all()
		models=chain(fields,apartments)
		models=sorted(models,key=operator.attrgetter("submitted"))
		models.reverse()
	
	paginator=Paginator(models,3)
	page=request.GET.get("page")
	try:
		models=paginator.page(page)
	except PageNotAnInteger:
		models=paginator.page(1)
	except EmptyPage:
		models=paginator.page(paginator.num_page)
	return(render(request,"estate/homepage.html",{"models":models,"page":page,"apartment_home_page_form":apartment_home_page_form}))

@login_required(login_url=reverse_lazy("login"))
def estateDetail_view(request,slug,model):
	if(model=="apartment"):
		specific_estate=apartment.objects.get(estate_slug=slug)
		tags=apartment.tags.all()
	if(model=="field"):
		specific_estate=field.objects.get(estate_slug=slug)
		tags=field.tags.all()
	return(render(request,"estate/estateDetail.html",{"estate":specific_estate,"tags":tags}))

@login_required(login_url=reverse_lazy("login"))
def fieldSubmit_view(request):
	if(request.method=="POST"):
		form=field_form(data=request.POST,files=request.FILES)
		if(form.is_valid()):
			new_field=form.save(commit=False)
			new_field.name=request.user.username
			new_field.estate_slug=f"{request.user.username}-{timezone.now().year}-{timezone.now().month}-{timezone.now().day}-{timezone.now().hour}-{timezone.now().minute}-{timezone.now().second}"
			new_field.save()
	else:
		form=field_form()
	return(render(request,"estate/estateSubmit.html",{"form":form}))

@login_required(login_url=reverse_lazy("login"))
def apartmentSubmit_view(request):
	if(request.method=="POST"):
		form=apartment_form(data=request.POST,files=request.FILES)
		if(form.is_valid()):
			new_apartment=form.save(commit=False)
			new_apartment.name=request.user.username
			new_apartment.estate_slug=f"{request.user.username}-{timezone.now().year}-{timezone.now().month}-{timezone.now().day}-{timezone.now().hour}-{timezone.now().minute}-{timezone.now().second}"
			new_apartment.save()
	else:
		form=apartment_form()
	return(render(request,"estate/estateSubmit.html",{"form":form}))

from django.http import HttpResponse
def homePageFilter_view(request):
	if("apartment" in request.GET):
		if(request.method=="POST"):
			form=apartment_home_page_form(request.POST,initial={"min_price":1000,"max_price":1000})
			models=apartment.objects.all()
			if(form.is_valid()):
				cd=form.cleaned_data
				if(cd["min_price"]):
					models=models.filter(price__gt=cd["min_price"])
				if(cd["max_price"]):
					models=models.filter(price__lte=cd["max_price"])
				if(cd["max_area"]):
					models=models.filter(area__lte=cd["max_area"])
				if(cd["min_area"]):
					models=models.filter(area__gt=cd["min_area"])
		else:
			models=apartment.objects.all()
			form=apartment_home_page_form()

	if("field" in request.GET):
		if(request.method=="POST"):
			form=field_home_page_form(request.POST,initial={"min_price":1000,"max_price":1000})
			models=field.objects.all()
			if(form.is_valid()):
				cd=form.cleaned_data
				if(cd["min_price"]):
					models=models.filter(price__gt=cd["min_price"])
				if(cd["max_price"]):
					models=models.filter(price__lte=cd["max_price"])
				if(cd["max_area"]):
					models=models.filter(area__lte=cd["max_area"])
				if(cd["min_area"]):
					models=models.filter(area__gt=cd["min_area"])
		else:
			models=field.objects.all()
			form=field_home_page_form()
	return(render(request,"estate/homepage.html",{"models":models,"form":form,"apartment_fields":True}))
