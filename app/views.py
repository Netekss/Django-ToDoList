from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CreateUserForm, TaskAdd
from .models import Person, Task


@login_required(login_url='login')
def index(request):
    user = request.user.get_username()

    tasks = Task.objects.filter(person=request.user.person)
    tasks_completed = Task.objects.filter(person=request.user.person, complete=True)

    form_add = TaskAdd()

    context = {'tasks': tasks,
               'form_add': form_add,
               'user': user,
               'tasks_completed': tasks_completed,
               }

    return render(request, 'app/index.html', context)


@login_required(login_url='login')
@require_POST
def task_add(request):
    form = TaskAdd(request.POST)

    if form.is_valid():
        new_task = Task(
            person=request.user.person,
            text=request.POST['text'],
        )
        new_task.save()

    return redirect('index')


@login_required(login_url='login')
def task_complete(request, id):
    task = Task.objects.get(pk=id)
    task.complete = True
    task.save()
    return redirect('index')


@login_required(login_url='login')
def task_delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('index')


@login_required(login_url='login')
def task_delete_completed(request):
    task = Task.objects.filter(person=request.user.person, complete=True)
    task.delete()
    return redirect('index')


@login_required(login_url='index')
def task_delete_all(request):
    task = Task.objects.filter(person=request.user.person)
    task.delete()
    return redirect('index')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,
                                username=username,
                                password=password
                                )

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'app/login.html', context)


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username.title()}')
                Person.objects.create(
                    user=user,
                    name=user.username,
                    email=user.email,
                )
                return redirect('login')
            else:
                messages.error(request, 'Something went wrong, please try again')

        context = {'form': form}
        return render(request, 'app/register.html', context)
