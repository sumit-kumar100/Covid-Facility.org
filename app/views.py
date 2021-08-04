from django.shortcuts import render
from .models import Service,State,City,Hospital,Availability
import time
from django.http import HttpResponse
# Create your views here.

def index(request):
    selected_state_id = request.GET.get('state')
    selected_city_id = request.GET.get('city')
    selected_service_id = request.GET.get('service')
    

    # Practice
    '''
    h = Hospital.objects.get(city=1)
    print(h.city.state)'''

    # Filtering states and cities vice versa
    cities = City.objects.all()
    states = State.objects.all()
    hospitals = Hospital.objects.all()


    if selected_state_id:
        time.sleep(0.01)
        cities = City.objects.filter(state=selected_state_id)


    if selected_state_id:
        if selected_city_id:
            hospitals = Hospital.objects.filter(city=City(id=selected_city_id),state=State(id=selected_state_id))
        else:
            hospitals = Hospital.objects.filter(state=State(id=selected_state_id))
    elif selected_city_id:
        if selected_state_id:
            hospitals = Hospital.objects.filter(city=City(id=selected_city_id),state=State(id=selected_state_id))
        else:
            hospitals = Hospital.objects.filter(city=City(id=selected_city_id))
    else:
        pass

    


    # filtering by services
    services = Service.objects.all().order_by('id')

    if selected_service_id:
        try:
            availabilities = Availability.objects.filter(service=Service(id=selected_service_id),hospital__city=City(id=selected_city_id),available__gt = 0)
        except:
            availabilities = Availability.objects.filter(service=Service(id=selected_service_id),available__gt = 0)
        hospitals = []
        for avail in availabilities:
            hospitals.append(avail.hospital)
        
    context = {
        'services':services,
        'states':states,
        'cities':cities,
        'hospitals':hospitals,
        'selected_state_id':selected_state_id,
        'selected_city_id':selected_city_id,
        'selected_service_id':selected_service_id
    }

    return render(request,'app/index.html',context=context)


def hospital_page(request,pk):
    context = {
        'hospital':Hospital.objects.get(id=pk)
    }
    return render(request,'app/hospital_page.html',context=context)


def about(request):
    return render(request,'app/about.html')


def contact(request):
    return render(request,'app/contact.html')