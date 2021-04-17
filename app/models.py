from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError


User = settings.AUTH_USER_MODEL

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,default=None,blank=True,on_delete=models.CASCADE)
    email=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)


    def __str__(self):
        return str(self.user.username)

class UserProject(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.title)

class UserTasks(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    project = models.ForeignKey(UserProject, default=None, on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True)
    start = models.TimeField(default=None)
    end = models.TimeField(default=None)
    duration = models.CharField(max_length=200,default=None,blank=True)
    timeup=models.BooleanField(default=False)
    

    def clean(self):
        if self.start > self.end:
            raise ValidationError('Start should be before end')
        return super().clean()

    def __str__(self):
        return str(self.title)





    



