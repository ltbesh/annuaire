from urllib2 import URLError

from django.views.generic import ListView, DetailView
from Course.models import Course, Place
from Course.forms import AddressForm
from geopy.geocoders import GoogleV3
from geopy.geocoders.google import GQueryError
from django.shortcuts import render_to_response
from django.contrib.gis import geos
from django.contrib.gis import measure
from django.template import RequestContext


class CourseListView(ListView):
	model = Course

class CourseDetailView(DetailView):
	model = Course



def get_places(latitude, longitude, radius):
	current_location = geos.fromstr("POINT(%s %s)" % (latitude, longitude))
	distance_from_point = {'m':radius}
	places = Place.gis.filter(location__distance_lte=(current_location, measure.D(**distance_from_point)))
	places = places.distance(current_location).order_by('distance')
	return places.distance(current_location)

def geocode_address(address):
    address = address.encode('utf-8')
    geocoder = GoogleV3()
    try:
        _, latlon = geocoder.geocode(address)
    except(URLError, GQueryError, ValueError):
        return None
    else:
        return latlon

def home(request):
	address_form = AddressForm()
	places = []
	if(request.POST):
		address_form = AddressForm(request.POST)
		if address_form.is_valid():
			address = address_form.cleaned_data['address']
			city = address_form.cleaned_data['city']
			radius = address_form.cleaned_data['radius']
			address = address + ' , ' + city
			location = geocode_address(address)
			if location:
				latitude, longitude = location
				places = get_places(latitude, longitude, radius)

	return render_to_response(
		'home.html', 
		{'form': address_form, 'places' : places },
		context_instance=RequestContext(request)
		)
