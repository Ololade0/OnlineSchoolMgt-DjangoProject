from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from app.forms import addAttendanceform, addMarksform, addNoticeform, createuserform
from app.models import *


def home(request):
    notice = Notice.objects.all()
    attendance = Attendance.objects.all()
    marks = Marks.objects.all()

    context = {
        'notice': notice,
        'marks': marks,
        'attendance': attendance,
    }
    return render(request, 'school/home.html', context)


def addAttendance(request):
    if request.user.is_authenticated:
        form = addAttendanceform()
        if request.method == 'POST':
            form = addAttendanceform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'school/addAttendance.html', context)
    else:
        return redirect('home')


def addMarks(request):
    if request.user.is_authenticated:
        form = addMarksform()
        if request.method == 'POST':
            form = addMarksform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'school/addMarks.html', context)
    else:
        return redirect('home')
#

def addNotice(request):
    if request.user.is_authenticated:
        form = addNoticeform()
        if request.method == 'POST':
            form = addNoticeform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'school/addNotice.html', context)
    else:
        return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'school/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'school/login.html', context)
#
#
def logoutPage(request):
    logout(request)
    return redirect('/')
