from django import forms
from .models import Question,Answers

class QuestionForms(forms.ModelForm):
     class Meta:
      model = Question
      exclude = ('Author',)


class AnswersForms(forms.ModelForm):

     class Meta:
      model = Answers
      fields = ['Answer']