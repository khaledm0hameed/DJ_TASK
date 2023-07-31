from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

'''
Author
question
tags
created_at
Content
________________________________

Author
Answer
question
created_at
'''



class Question(models.Model):
    Author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateField(default=timezone.now)
    tags = TaggableManager()
    question = models.CharField(max_length=20000)
    Content = models.CharField(max_length=20000)


class Answers(models.Model):
    Author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateField(default=timezone.now)
    Answer = models.CharField(max_length=1000)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="Answers_Question")
