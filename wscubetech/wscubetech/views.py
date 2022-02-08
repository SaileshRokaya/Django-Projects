from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data={
        'title':'Home new Page',
        'bdata':"Welcome to SBRC Nepal",
        'clist':['PHP','Java', 'Django'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'pradeep', 'phone':9813065077},
            {'name':'Sailesh','phone':9843620536},
            {'name':'Bikash','phone':981362025}
        ]
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("Welcome to SBRC Nepal")

def Course(request):
    return HttpResponse("Welcome to SBRC Course")

def CourseDetails(request, courseid):
    return HttpResponse(courseid)
