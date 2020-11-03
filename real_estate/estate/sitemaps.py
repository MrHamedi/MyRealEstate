from django.contrib.sitemaps import Sitemap 
from .models import field,apartment

class fieldSiteMap(Sitemap):
	priority=0.8
	changefreq="always"
	def items(self):
		return(field.objects.all())
	def lastmod(self,obj):
		return(obj.update) 

class apartmentSiteMap(Sitemap):
	priority=0.8
	changefreq="daily"
	def items(self):
		return(apartment.objects.all())
	def lastmod(self,obj):
		return(obj.update)