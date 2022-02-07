from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data={
        'title':'Home new Page'
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("<b>Welcome to SBRC Nepal</b>")

def Course(request):
    return HttpResponse("Welcome to SBRC Course")

def CourseDetails(request, courseid):
    return HttpResponse(courseid)
