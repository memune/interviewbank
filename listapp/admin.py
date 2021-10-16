from django.contrib import admin

# Register your models here.
from listapp.models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'like', 'writer', 'created_at']

admin.site.register(Question, QuestionAdmin)