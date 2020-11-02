from estate.models import field,apartment
from django.shortcuts import render,get_object_or_404
from itertools import chain
from django.http import Http404,HttpResponseRedirect
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import field_form,apartment_form 
from django.utils import timezone
from datetime import datetime
import operator

def homePage_view(request):
	if("apartment" in request.GET):
		models=apartment.objects.all()
	elif("field" in request.GET):
		models=field.objects.all()
	else:
		apartments=apartment.objects.all()
		fields=field.objects.all()
		models=chain(fields,apartments)
		models=sorted(models,key=operator.attrgetter("submitted"))
		models.reverse()
	return(render(request,"estate/homepage.html",{"models":models}))

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
