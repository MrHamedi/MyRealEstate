from django.urls import path 
from .views import index,contactUs_view


urlpatterns = [
	path("contactUs/",contactUs_view,name="contact_us"),
	path("<str:pagename>/",index,name="index"),
]