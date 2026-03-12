from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from teams.models import TeamMember
from projects.models import Project
from tasks.models import Task


@login_required
def dashboard(request):

    user = request.user

    teams = TeamMember.objects.filter(user=user)

    projects = Project.objects.filter(team__teammember__user=user).distinct()

    tasks = Task.objects.filter(assigned_to=user)

    context = {
        'teams': teams,
        'projects': projects,
        'tasks': tasks
    }

    return render(request, 'dashboard/dashboard.html', context)