from django.shortcuts import render
from .models import page 
from django.core.mail import send_mail,get_connection
from .forms import contactUs_form
from django.contrib import messages

def index(request,pagename):
	permalink="/"+pagename
	index_page=page.objects.get(permalink=permalink)
	context={
		"title":index_page.title,
		"body":index_page.body,
	}
	return(render(request,"pages/index.html",context))

def contactUs_view(request):
	if(request.method=="POST"):
		form=contactUs_form(data=request.POST)
		if(form.is_valid()):	
			advice=form.cleaned_data
			advice['username']=str(request.user)
			send_mail(f"Advice",f"This advice is a feedback from {advice['username']} \n {advice['advice']}",advice["username"],["ahmadihamed167@gmail.com"],fail_silently=False)
	else:
		form=contactUs_form()
	return(render(request,"pages/contactUs_form.html",{"form":form}))
