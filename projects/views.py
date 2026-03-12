from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required
def project_list(request):

    user = request.user

    projects = Project.objects.filter(
        team__teammember__user=user
    ).distinct()

    context = {
        'projects': projects
    }

    return render(request, 'projects/project_list.html', context)