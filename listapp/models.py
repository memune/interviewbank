from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from positionapp.models import Position


class Question(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='question', null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, related_name='question', null=True)
    question = models.CharField(max_length=500, null=False)
    like = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.question


