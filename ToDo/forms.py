from django import forms
from .models import Tasks, Todo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["task", "is_completed"]

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
