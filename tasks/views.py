from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task



@login_required
def task_list(request):

    tasks = Task.objects.filter(assigned_to=request.user)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, id):

    task = get_object_or_404(Task, id=id, assigned_to=request.user)

    if request.method == "POST":

        status = request.POST.get("status")
        task.status = status
        task.save()

        return redirect('task_list')

    return render(request, 'tasks/task_detail.html', {'task': task})