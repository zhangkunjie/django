from _ast import Str
import json

from django.http.response import HttpResponse
from django.shortcuts import render
from ajax.models import Student
# Create your views here.
def index(request):
    return render(request,"index.html")
def getStudentInfo(request):
    id=request.GET['id']
    print("###############"+str(id))
    student=Student.objects.get(id=id)
    studentJSON=student.to_JSON2()
    print("################"+studentJSON)
    return HttpResponse(studentJSON, content_type='application/json')
