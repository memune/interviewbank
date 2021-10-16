from django.urls import path

from listapp.views import QuestionListView, QuestionCreateView

app_name = 'listapp'

urlpatterns = [
    path('', QuestionListView.as_view(), name='list'),
    path('create/', QuestionCreateView.as_view(), name='create'),
]