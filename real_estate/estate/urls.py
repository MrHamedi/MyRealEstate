from django.urls import path
from .views import homePage_view,estateDetail_view,apartmentSubmit_view,fieldSubmit_view,homePageFilter_view
from django.views.generic import TemplateView
from .sitemaps import fieldSiteMap,apartmentSiteMap
from django.contrib.sitemaps.views import sitemap
from .feeds import estateFeed

app_name="estate"
sitemaps = {"fieldSiteMap":fieldSiteMap,"apartmentSiteMap":apartmentSiteMap}

urlpatterns=[
	path("feed/estate/",estateFeed()),	
	path("submit/",TemplateView.as_view(template_name="pages/EstateChoose.html"),name="EstateChoose"),
	path("submit/field/",fieldSubmit_view,name="fieldSubmit"),
	path("submit/apartment/",apartmentSubmit_view,name="apartmentSubmit"),
	path("homePageFilter/",homePageFilter_view,name="homePageFilter"),
	path("",homePage_view,name="homepage"),
	path("<slug:slug>/<str:model>/",estateDetail_view,name="estate_detail"),
	path("sitemap.xml",sitemap,{"sitemaps":sitemaps},name="fieldSiteMap"),
]
