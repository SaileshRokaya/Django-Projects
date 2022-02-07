from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data={
        'title':'Home new Page',
        'bdata':"Welcome to SBRC Nepal"
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("Welcome to SBRC Nepal")

def Course(request):
    return HttpResponse("Welcome to SBRC Course")

def CourseDetails(request, courseid):
    return HttpResponse(courseid)
