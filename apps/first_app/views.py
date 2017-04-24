from django.shortcuts import render,redirect
from .models import Course,Description

def index(request):
    context ={'data':Course.objects.all()}
    return render(request,"first_app/index.html",context)
def createCourse(request):
    courseObject=Course.objects.create(name=request.POST['name'])
    Description.objects.create(description=request.POST['description'],course_id = courseObject)
    return redirect('/')
def removeCourse(request,id):
    courseObject = Course.objects.get(id=id)
    context = {'data':courseObject}
    return render(request,"first_app/deletequestion.html",context)
def destroyCourse(request,id):
    Course.objects.get(id=id).delete()
    return redirect('/')
