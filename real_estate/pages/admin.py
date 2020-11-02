from django.contrib import admin
from .models import page
 
class pageAdmin(admin.ModelAdmin):
	list_display=("title","permalink","create","modify")
	list_filter=("create",)
	search_fields=("title","permalink")

admin.site.register(page,pageAdmin)