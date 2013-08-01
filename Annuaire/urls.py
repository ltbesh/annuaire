from django.conf.urls import patterns, include, url


from Course.views import CourseListView, CourseDetailView

from Course import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name = 'home'),
	url(r'^course/$', CourseListView.as_view(), name = "course_list_view"),
	url(r'^course/(?P<pk>\d+)/', CourseDetailView.as_view(), name = "course_detail_view"),
	url(r'^search/', include('haystack.urls')),
    # Examples:
    # url(r'^$', 'Annuaire.views.home', name='home'),
    # url(r'^Annuaire/', include('Annuaire.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
