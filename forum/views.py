from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from .models import Question,Answers
from .forms import QuestionForms,AnswersForms
# Create your views here.

class Question_list(ListView):
    model = Question
    template_name = 'index.html'
    context_object_name = 'ques'



def Question_detail(request, pk):
    question = Question.objects.get(id=pk)
    Answer = Answers.objects.filter(question=question)

    if request.method == "POST":
        form = AnswersForms(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.Author = request.user
            myform.question = question  
            myform.save()
    else:
        form = AnswersForms()

    return render(request, 'detail.html', {'ques': question, 'form': form, 'Answer':Answer })


class Question_delet(DeleteView):
    model = Question
    success_url = '/'
    context_object_name = 'ques'
    

class Question_create(CreateView):
    model = Question
    fields =['created_at','tags','question','Content']
    success_url = '/'
    template_name ='add.html'

class Question_edit(UpdateView):
    model = Question
    fields =['created_at','tags','question','Content']
    success_url = '/'
    template_name ='add.html'
