from django.urls import path
from .views import home,todo_detail,add_task, add_todo, delete_task, task_completion


urlpatterns = [
   path("", home, name="home"),
   path("detail/<int:todo_id>/", todo_detail , name="detail"),
   path("detail/<int:todo_id>/add_task/", add_task, name="add-task"),
   path("add_todo", add_todo, name="add-todo"),
   path("detail/<int:todo_id>/task/<int:task_id>/delete", delete_task, name="delete-task"),
   path("task/<int:task_id>/toggle_completion", task_completion, name="task-completion")
]
