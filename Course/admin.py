from django.contrib import admin
from Course.models import Course, Price, Slot, Place, Note

admin.site.register(Course)
admin.site.register(Price)
admin.site.register(Slot)
admin.site.register(Place)
admin.site.register(Note)