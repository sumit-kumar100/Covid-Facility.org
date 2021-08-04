from django.contrib import admin
from django.db import models
from .models import State,City,Hospital,Service,Availability
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=Hospital)
def afterhospitalsave(signal,instance,**kwrg):
    services = Service.objects.all()
    for service in services:
        availabilities = Availability.objects.create(hospital=instance,service=service)
        availabilities.save()

@receiver(post_save,sender=Service)
def afterservicesave(signal,instance,**kwrg):
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
        availabilities = Availability.objects.create(hospital=hospital,service=instance)
        availabilities.save()

class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(State,StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name','state')
admin.site.register(City,CityAdmin)


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','state','city')
admin.site.register(Hospital,HospitalAdmin)


class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('title',)    
admin.site.register(Service,ServiceAdmin)


class AvailabilityAdmin(admin.ModelAdmin):
    models = Availability
    list_display = ('hospital','service','total','available')
admin.site.register(Availability,AvailabilityAdmin)