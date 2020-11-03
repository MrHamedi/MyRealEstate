from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import apartment,field 
import operator
from itertools import chain

class estateFeed(Feed):
	title="last estate and updates"
	description="This is a feed to represet the last estates news"
	link="/sitenews/"
	def items(self):
		apartments=apartment.objects.all()
		fields=field.objects.all()
		estates=chain(apartments,fields)
		estates=sorted(estates,key=operator.attrgetter("submitted"))
		estates.reverse()
		return(estates[:5])
	def item_title(self,obj):
		return(obj.title)
	def item_description(self,obj):
		return(obj.description)
	def item_link(self,obj):
		return(obj.get_absolute_url())