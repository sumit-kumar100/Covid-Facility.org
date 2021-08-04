from enum import Flag
from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False)
    state = models.ForeignKey(State , on_delete=models.CASCADE , related_name='citites')

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False)
    address = models.CharField(max_length=150 , null=False , blank=False)
    phone = models.IntegerField()
    city = models.ForeignKey(City , on_delete=models.CASCADE , related_name='hospitals')
    state = models.ForeignKey(State , on_delete=models.CASCADE ) 

    def __str__(self):
        return self.name
    


class Service(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.title



class Availability(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='availabilities')
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='availabilities')
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

