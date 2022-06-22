from django.urls import path
from . import views




#Create endpoints to the app
urlpatterns = [
    path('students/', views.getAllStudents , name="getAllStudents"),
    path('students/<int:id>/' , views.studentInfo ,  name="getStudentByID"),
]