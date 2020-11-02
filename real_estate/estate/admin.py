from django.contrib import admin 
from .models import apartment,field

class fieldAdmin(admin.ModelAdmin):
	prepopulated_fields={"estate_slug":("name","price","area")}
	list_display=("title","name","price","meterPrice","submitted","estate_slug")
	list_filter=("price","name","area")
	ordering=("-submitted",)
	search_fields=("name",)
	fieldsete=(
		(None,{"fields":("name","title","tags")})
		)

class apartmentAdmin(admin.ModelAdmin):
	list_display=("name","renter","phone","price")
	list_filter=("name","price","area","status")
	search_fields=("name","renter")
	prepopulated_fields={"estate_slug":("name","price","area")}
	fieldsets=(
		(None,{"fields":("name","title","estate_slug","description","tags")}),
		("Trade information",{"fields":("trade_type","price","meterPrice"),"classes":("collapse",)}),
		("Apartment information",{"fields":("adress","rooms","floor","floors","document","area"),"classes":("collapse",)}),
		("Contact information",{"fields":("phone","renter_phone","parking","heating_system","cooler","email"),"classes":('collapse',),}),
		("Apartment material",{"fields":("floor_material","cabinet"),"classes":("collapse",)}),
		("images",{"fields":("image1","image2","image3","image4"),"classes":("collapse",)})
)


admin.site.register(field,fieldAdmin)
admin.site.register(apartment,apartmentAdmin)