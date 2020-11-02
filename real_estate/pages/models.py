from django.db import models

class page(models.Model):
	title=models.CharField(max_length=200)
	body=models.TextField()
	permalink=models.CharField(max_length=30,unique=True)
	create=models.DateField(auto_now_add=True)
	modify=models.DateField(auto_now=True)