from django.db import models 
from django.urls import path, include


# Create your models here.

class Contact(models.Model):
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	priemail = models.EmailField(max_length=100)
	extemail = models.EmailField(max_length=100)
	jobdesc = models.TextField(max_length=50)
	phone = models.CharField(max_length=50)
	address = models.TextField(max_length=200)
	message = models.TextField(max_length=200)
	timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
