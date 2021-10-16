from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView

from listapp.forms import QuestionCreationForm
from listapp.models import Question


class QuestionListView(ListView):
    model = Question
    context_object_name = 'question_list'
    template_name = 'listapp/question_list.html'
    paginate_by = 10

class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionCreationForm
    template_name = 'listapp/question_create.html'

    def form_valid(self, form):
        temp_question = form.save(commit=False)
        temp_question.writer = self.request.user
        temp_question.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('listapp:list')