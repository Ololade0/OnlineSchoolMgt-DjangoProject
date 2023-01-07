from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vname='home'),
   
    path('addAttendance/', addAttendance,name='addAttendance'),
   
    path('addMarks/', addMarks,name='addMarks'),
 
    path('addNotice/', addNotice,name='addNotice'),
 
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),

]