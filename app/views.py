from django.shortcuts import render

from app.models import *


def home(request):
    notice = Notice.objects.all()
    attendance = Attendance.objects.all()
    marks = Marks.objects.all()
 
    context = {
        'notice':notice,
        'marks':marks,
        'attendance':attendance,
    }
    return render(request,'school/home.html',context)
