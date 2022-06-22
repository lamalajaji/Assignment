from django.db import models



# Create the student model
# Django model class has default field with name id which is auto increment Field. 
class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentNumber = models.CharField(max_length=10)
    facultyName = models.CharField(max_length=100)



# This function to make the student name show to the admin in the dashboard
    def __str__(self):
        return self.studentName
   

