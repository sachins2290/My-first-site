from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Personalinfo(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	postalcode = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	#created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
            
	
	#def publish(self):
        #self.published_date = timezone.now()
        #self.save()

    #def __str__(self):
        #return self.last_name

# Create your models here.
