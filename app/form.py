from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

        

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProjectForm(ModelForm):
    class Meta:
        model=UserProject
        fields=['title']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Project Title'}),
        }
        

class TaskForm(ModelForm):
    class Meta:
        model=UserTasks
        fields=['title','start','end']
        widgets={
            'start': forms.TimeInput(attrs={'type': 'time','class':'form-control mb-2 mr-sm-2'}),
            'end': forms.TimeInput(attrs={'type': 'time','class':'form-control mb-2 mr-sm-2' }),
            'title':forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Task Title'}),
        }
        
    
        
        
      
