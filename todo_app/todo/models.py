from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150,blank=True)
    description = models.TextField(max_length=200,blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title