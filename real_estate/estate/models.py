from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

state_document=(("six","six tone"),("without","without document"))
class estate(models.Model):
	name=models.CharField(max_length=200,default="REAL ESTATE")
	submitted=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now=True)
	adress=models.TextField(blank=True)
	phone=models.CharField(max_length=30)
	email=models.EmailField(blank=True)
	area=models.DecimalField("area in square meters ",max_digits=5,decimal_places=1)
	price=models.BigIntegerField()
	meterPrice=models.BigIntegerField("each sqaure meters price")
	image1=models.ImageField(blank=True)
	image2=models.ImageField(blank=True)
	image3=models.ImageField(blank=True)
	image4=models.ImageField(blank=True)
	estate_slug=models.SlugField(unique_for_date="submitted",max_length=250,blank=True)
	document=models.CharField(max_length=200,choices=state_document)
	title=models.CharField(max_length=400)
	description=models.TextField(blank=True)
	tags=TaggableManager()
	class Meta:
		abstract=True
		ordering=("-submitted",)
	def __str__(self):
		return(self.title)
	def get_absolute_url(self):
		return(reverse("estate:estate_detail",args=[self.estate_slug,self.model]))

buildSides=(("one","one side"),("two","both side"),("none","neither of sides"))
class field(estate):
	length=models.DecimalField(max_digits=5,decimal_places=2)
	width=models.DecimalField(max_digits=5,decimal_places=2)
	build_sides=models.CharField("how many of sides have been built",choices=buildSides,max_length=200)
	front_progress=models.IntegerField()
	back_progress=models.IntegerField()
	max_allowed_floors=models.IntegerField("count of allowed floors to build")
	model="field"


status_choices=(("owner","in owner Residence"),("rent","in rent"),("empty","empty"))
heating_systems=(("radiator","Rediator"),("heater","Heater"))
cooler_systems=(("wet","wet cooler"),("spilet","spilet"))
trade_type=(("S","sell"),("R","rent"),("pre","pree-sell"))
class apartment(estate):
	renter=models.CharField(max_length=200,blank=True)
	renter_phone=models.CharField(max_length=60,blank=True)
	floor=models.IntegerField("unit is in which floor of apartment",)
	floors=models.IntegerField("The max count of floors")
	floor_material=models.CharField(max_length=200)
	cabinet=models.CharField(max_length=200)
	phone=models.IntegerField()
	parking=models.IntegerField()
	rooms=models.IntegerField()
	status=models.CharField(choices=status_choices,max_length=200)
	heating_system=models.CharField(max_length=200,choices=heating_systems)
	cooler=models.CharField(max_length=200,choices=cooler_systems)
	trade_type=models.CharField(choices=trade_type,max_length=200)
	model="apartment"