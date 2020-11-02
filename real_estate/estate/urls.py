from django.urls import path
from .views import homePage_view,estateDetail_view,apartmentSubmit_view,fieldSubmit_view
from django.views.generic import TemplateView

app_name="estate"

urlpatterns=[
	path("submit/",TemplateView.as_view(template_name="pages/EstateChoose.html"),name="EstateChoose"),
	path("submit/field/",fieldSubmit_view,name="fieldSubmit"),
	path("submit/apartment/",apartmentSubmit_view,name="apartmentSubmit"),
	path("",homePage_view,name="homepage"),
	path("<slug:slug>/<str:model>/",estateDetail_view,name="estate_detail"),
	#path("submit/",estateSubmit_view,name="submit"),
]
