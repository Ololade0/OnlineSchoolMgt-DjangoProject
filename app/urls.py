from django.contrib import admin
from django.urls import include, path
from . import views
from .views import loginPage, addAttendance, addMarks, logoutPage, registerPage, addNotice

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
   
    path('addAttendance/', views.addAttendance,name='addAttendance'),
    path('addMarks/', addMarks,name='addMarks'),
    path('addNotice/', addNotice,name='addNotice'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),

]