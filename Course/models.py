from urllib2 import URLError

from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.db import models
from django.contrib.auth.models import User
from geopy.geocoders import GoogleV3
from geopy.geocoders.google import GQueryError

# Create your models here.
class Course(models.Model):
    description = models.TextField()
    equipment = models.TextField()
    contact_phone_number = models.CharField(max_length = 15)
    contact_email = models.EmailField()
    price_clarification = models.TextField()

class Price(models.Model):
    
    DURATION = (
        (1, "slot"),
        (2, "month"),
        (3, "trimester"),
        (4, "year"),
    )

    price = models.IntegerField()
    duration = models.CharField(choices = DURATION, max_length = 20)
    course = models.ForeignKey(Course)

class Slot(models.Model):
    WEEKDAYS = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    )

    LEVEL = (
        (1, 'beginner'),
        (2, 'intermediate'),
        (3, 'advanced'),
    )

    weekday_from = models.IntegerField(choices=WEEKDAYS)
    weekday_to = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    level = models.IntegerField(choices = LEVEL)
    children_accepted = models.BooleanField()
    adult_accepted = models.BooleanField()

class Place(models.Model):
    name = models.CharField(max_length = 200)
    adress = models.CharField(max_length = 300)
    zip_code = models.CharField(max_length = 5)
    city = models.CharField(max_length = 100)

    location = gis_models.PointField(u"longitude/latitude",geography=True, blank=True, null=True)

    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        if not self.location:
            adress = u'%s %s' % (self.city, self.adress)
            adress = adress.encode('utf-8')
            geocoder = GoogleV3()
            try:
                _, latlon = geocoder.geocode(adress)
            except(URLError, GQueryError, ValueError):
                pass
            else:
                point = "POINT(%s %s)" % (latlon[0], latlon[1])
                self.location = geos.fromstr(point)
        super(Place, self).save()

class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title
