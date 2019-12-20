from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='+', on_delete=models.SET_NULL, null=True)

class Task(models.Model):
    class Status(models.IntegerChoices):
        NEW = 1
        DOING = 2
        DONE = 3

    class Priority(models.IntegerChoices):
        LOW = 3
        MEDIUM = 2
        HIGH = 1
    
    class TaskType(models.IntegerChoices):
        FRONTEND = 1
        BACKEND = 2

    name = models.CharField(max_length=32)
    description = models.TextField()
    status = models.IntegerField(choices=Status.choices)
    priority = models.IntegerField(choices=Priority.choices)
    task_type = models.IntegerField(choices=TaskType.choices)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='+', on_delete=models.SET_NULL, null=True)
    

class Bug(models.Model):

    class Status(models.IntegerChoices):
        NEW = 1
        FIXING = 2
        FIXED = 3

    name = models.CharField(max_length=32)
    description = models.TextField()
    status = models.IntegerField(choices=Status.choices)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='+', on_delete=models.SET_NULL, null=True)