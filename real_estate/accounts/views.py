from django.shortcuts import render 
from .models import profile
from .forms import profile_form,register_form
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy,reverse
from .models import profile
from django.contrib.auth.models import User

def register_view(request):
	if(request.method=="POST"):
		form=register_form(request.POST)
		if(form.is_valid()):
			new_user=form.save()
			new_profile=profile(user=new_user)
			new_profile.save()
			return(HttpResponseRedirect(f"accounts/profile_update/{new_user.id}/"))
			return(render(request,"registration/register.html",{"form":form}))
		else:
			#return(reverse("user_register"))
			return(render(request,"registration/register.html",{"form":form}))

	else:
		form=register_form()
		return(render(request,"registration/register.html",{"form":form}))


def profileUpdate_view(request):
	if(request.method=="POST"):
		user_form=register_form(instance=request.user,data=request.POST,)
		userProfile_form=profile_form(request.POST,instance=request.user.profile,files=request.FILES)
		if(userProfile_form.is_valid() and user_form.is_valid()):
			userProfile_form.save()
			user_form.save()
	else:
		user_form=register_form(instance=request.user)
		userProfile_form=profile_form(instance=request.user.profile)
	return(render(request,"registration/profileEdit.html",{"user_form":user_form,"profile_form":userProfile_form}))

class profile_view(DetailView):
	model=User
	template_name="accounts/profile.html"
	context_object_name="user"