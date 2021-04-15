from django.db import models

# Create your models here.

class form_tb(models.Model):
	firstname=models.CharField(max_length=20,default='')
	
	email=models.CharField(max_length=20,default='')
	password=models.CharField(max_length=20,default='')

	dob=models.CharField(max_length=10,default='')
	phone=models.CharField(max_length=10,default='')
	address=models.CharField(max_length=50,default='')
	city=models.CharField(max_length=15,default='')
	state=models.CharField(max_length=15,default='')
	country=models.CharField(max_length=15,default='')
