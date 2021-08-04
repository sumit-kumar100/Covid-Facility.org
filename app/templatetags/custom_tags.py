from django import template
from app.models import Availability, Hospital

register = template.Library()


@register.filter(name='get_data')
def get_data(hospital_id):
    data = Availability.objects.filter(hospital=hospital_id).order_by('service_id')
    return data



@register.filter(name='is_selected')
def is_state_selected(state_id,state_selected):
    if str(state_id) == str(state_selected):
        return 'selected'
    return ''