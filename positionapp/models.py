from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
