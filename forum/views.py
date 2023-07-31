from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from .models import Question,Answers
# Create your views here.

class Question_list(ListView):
    model = Question
    template_name = 'index.html'
    context_object_name = 'ques'