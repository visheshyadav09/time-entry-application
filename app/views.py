from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse,JsonResponse

# Create your views here.
from .form import RegisterForm,ProjectForm,TaskForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='app:login')
def homeview(request):
    tasks=UserTasks.objects.filter(user=request.user)
    return render(request,'app/home.html',{'tasks':tasks})


def registerview(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            
            email=form.cleaned_data.get('email')
            Customer.objects.create(
                        user=user,
                        email=email
                    )
            messages.success(request,"Account was created for "+username)
            return redirect('app:login')
        else:
            messages.info(request,"Incorrect Data Input, Please fill form again.")
            return redirect('app:register')
    return render(request,'app/index.html',{'form':form})
    

            # else: 
            #     # Invalid form! Reshow the form with error highlighted 
            #     return render(request, ) 

def loginview(request):
    context={}
    if request.method=='POST':    
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('app:home')
        else:
            messages.info(request,'Username or Password Incorrect!')
            return redirect('app:login')
    return render(request,'app/login.html',context)

@login_required(login_url='app:login')
def addproject(request):
    
    name=request.user
    print(name)
    form=ProjectForm()
    if request.method=="POST":
        
        form=ProjectForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
        
        return redirect('app:home')
    return render(request,'app/add_project.html',{'form':form})
    
@login_required(login_url='app:login')
def addTask(request):
    form=TaskForm()
    projects=UserProject.objects.filter(user=request.user)
    if request.method=='POST':
        print(1)
        form=TaskForm(request.POST)
        if form.is_valid():
            print(1)
            instance=form.save(commit=False)
            instance.project =UserProject.objects.get(user=request.user,title=request.POST['project'])
            instance.user=request.user
            instance1=form.cleaned_data['start']
            instance2=form.cleaned_data['end']
            print(instance2)
            duration=difft(instance1,instance2)
            time_string = str(duration)+' min'
            instance.duration= time_string    
            instance.save()
            return redirect('app:home')
        else:
            messages.info(request,"Start time should be before end time")
            return redirect('app:task')
    return render(request,'app/add_task.html',{'form':form,'projects':projects})
    


def logoutUser(request):
    logout(request)
    return redirect('app:login')
    
@login_required(login_url='app:login')
def taskDetail(request,id):
    task=UserTasks.objects.get(id=id)
    if request.is_ajax():
       if(request.POST['data']=='timeup'):
           UserTasks.objects.filter(title=task.title).update(timeup=True)
         
           return JsonResponse('Field Updated',safe=False)
       
    return render(request,'app/taskdetail.html',{'task':task})
    
def difft(start,end):
    a,b, = start.hour, start.minute 
    w,x = end.hour, end.minute
    delt = (w-a)*60 + (x-b)
    return delt

      
