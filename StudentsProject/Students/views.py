from .models import Student
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import ItemSerializer




# This Function will do (GET / POST) methods on students data
@api_view(['GET' , 'POST'])
def getAllStudents(request):
    students = Student.objects.all()

    if request.method == 'GET' :
        serializer = ItemSerializer(students , many = True)
        return Response(serializer.data)



    if request.method == 'POST':
        serializer = ItemSerializer( data= request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data , status= status.HTTP_201_CREATED)


   



# This Function take ID number as params, and return student with that ID and do (GET / PUT / DELETE ) methods
   
@api_view(['GET' ,'PUT' ,'DELETE'])
def studentInfo(request , id):
    student = Student.objects.get(id=id)

    if request.method == 'GET':
        try: 
           serializer = ItemSerializer(student)
           return Response(serializer.data)
        except Student.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)



    elif request.method == 'PUT':
        serializer = ItemSerializer(student , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

