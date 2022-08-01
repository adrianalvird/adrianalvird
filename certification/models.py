from django.db import models

# Create your models here.

class Certification(models.Model):
	img = models.FileField(upload_to='certificates')
	certname = models.CharField(max_length=50)
	tagone = models.CharField(max_length=20)
	tagtwo = models.CharField(max_length=20)
	
	
