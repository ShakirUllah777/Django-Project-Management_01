from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):

    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    start_date = models.DateField()
    due_date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title