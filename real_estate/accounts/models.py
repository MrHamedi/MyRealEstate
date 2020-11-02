from django.conf import settings
from django.db import models 


class profile(models.Model):
	email=models.EmailField()
	name=models.CharField(max_length=100)
	family=models.CharField(max_length=100)
	image=models.ImageField(blank=True,upload_to="Y/m/d/profile/")
	phone=models.CharField(max_length=100)
	user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")
