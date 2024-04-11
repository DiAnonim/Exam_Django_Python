from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Система управления задачами (Task Management System):
# Разработайте приложение, которое позволит пользователям создавать задачи,
# устанавливать приоритеты, добавлять комментарии и присваивать задачи другим 
# пользователям. Можно также добавить функционал уведомлений 
# о сроках выполнения задач



class Todo(models.Model):
    
    class TodoStatus(models.TextChoices):
        CREATED = "C", "created"
        IN_PROGRESS = "I", "in progress"
        DONE = "D", "done"
        
    class TodoPriority(models.TextChoices):
        LOW = "L", "low"
        MEDIUM = "M", "medium"
        HIGH = "H", "high"
    
    image = models.ImageField(upload_to="todo_images/", null=True, blank=True, verbose_name="Image", default="todo_images/default.jpg")
    title = models.CharField(max_length=100, verbose_name="Title", validators=[validators.MinLengthValidator(5, "Title must be greater than 5 charapters")])
    text = models.TextField(blank=True, verbose_name="Body", validators=[validators.MinLengthValidator(20, "Body must be greater than 20 charapters")])
    created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Created")
    datecompleted = models.DateTimeField(null=True, blank=True, verbose_name="Completed")
    important = models.CharField(max_length=1, choices=TodoPriority.choices, default=TodoPriority.LOW, verbose_name="Priority")
    status = models.CharField(max_length=1, choices=TodoStatus.choices, default=TodoStatus.CREATED, verbose_name="Status")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author", related_name="todos")
    perform = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Perform", related_name="perform", null=True, blank=True)
    
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-important"]
        
        
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="Author")
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="comments", verbose_name="Task")
    text = models.TextField( verbose_name="Text")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    
    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
