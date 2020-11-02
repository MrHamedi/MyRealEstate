from django.contrib import admin 
from .models import profile

class profileAdmin(admin.ModelAdmin):
	list_display=("user","name","family","email","phone")

admin.site.register(profile,profileAdmin)