from . import views

from django.urls import path,include

app_name = "app"
urlpatterns = [
    path('',views.homeview ,name='home'),
    path('project/',views.addproject,name='project'),
    path('register/',views.registerview ,name='register'),
    path('login/',views.loginview,name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('task/',views.addTask,name='task'),
    path('taskdetail/<id>',views.taskDetail,name='taskdetail')
    

]