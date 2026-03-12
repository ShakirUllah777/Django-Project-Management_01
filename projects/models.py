from django.db import models
from django.contrib.auth.models import User
from teams.models import Team


class Project(models.Model):

    STATUS_CHOICES = (
        ('planning', 'Planning'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    start_date = models.DateField()
    deadline = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name