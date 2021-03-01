from django.contrib import admin
from .models import Service, Request, Project, Contact
# Register your models here.


admin.site.register(Service)
admin.site.register(Request)
admin.site.register(Project)
admin.site.register(Contact)
