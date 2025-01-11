from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class Tasks(models.Model):
    todo = models.ForeignKey(Todo, related_name="tasks", on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task