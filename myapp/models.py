from django.db import models

# Create your models here.
class ToDoS(models.Model):
    name = models.TextField()