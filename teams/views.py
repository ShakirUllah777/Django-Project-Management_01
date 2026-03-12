from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TeamMember


@login_required
def team_list(request):

    teams = TeamMember.objects.filter(user=request.user)

    return render(request, 'teams/team_list.html', {'teams': teams})


@login_required
def team_detail(request, id):

    members = TeamMember.objects.filter(team_id=id)

    return render(request, 'teams/team_detail.html', {'members': members})