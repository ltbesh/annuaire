from django.views.generic import ListView, DetailView
from Course.models import Course

class CourseListView(ListView):
	model = Course

class CourseDetailView(DetailView):
	model = Course
