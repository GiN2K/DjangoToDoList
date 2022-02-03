from django.db import models

# Create your models here.
class Todomodel(models.Model):
    todo_item = models.CharField(max_length=100,default="")
    
    def __str__(self):
        return self.todo_item