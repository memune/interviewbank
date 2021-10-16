from django.forms import ModelForm
from django import forms

from listapp.models import Question
from positionapp.models import Position


class QuestionCreationForm(ModelForm):

    position = forms.ModelChoiceField(queryset=Position.objects.all(), required=True)

    class Meta:
        model = Question
        fields = ['question', 'position']


