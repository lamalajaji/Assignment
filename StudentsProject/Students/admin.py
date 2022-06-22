from django.contrib import admin
from .models import Student


#This for give admin the access to add new students
admin.site.register(Student)

