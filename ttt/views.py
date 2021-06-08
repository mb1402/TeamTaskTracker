from django.shortcuts import render, redirect
from django.forms import inlineformset_factory, formset_factory
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import TaskCreateForm, TaskUpdateForm, CreateUserForm
from .models import *

# Create your views here.





def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('login')

	context = {'form':form}
	return render(request, 'ttt/register.html', context)





def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect('home')


	return render(request, 'ttt/login.html')


def logoutPage(request):




	return render(request, 'ttt/logout.html')


def home(request):
	members = Member.objects.all()
	tasks = Task.objects.all()
	task_details = Allocation.objects.all()

	total_tasks = tasks.count()
	tasks_pending = tasks.filter(task_status='In Progress')
	task_pending_count = tasks_pending.count()
	tasks_completed = tasks.filter(task_status='Completed').count()

	context = {
		'tasks':tasks,
		'members':members,
		'total_tasks':total_tasks,
		'tasks_pending':tasks_pending,
		'tasks_completed':tasks_completed,
		'task_pending_count': task_pending_count,
		'task_details' : task_details

	}

	return render(request, 'ttt/dashboard.html', context)



def member(request, pk_test):
	members = Member.objects.get(id=pk_test)
	task_details = Allocation.objects.filter(member__id=pk_test)


	task_count = task_details.count()

	context = {
		'members':members,
		'task_details' : task_details,
		'task_count':task_count

	}

	return render(request, 'ttt/member.html', context)



def view_task(request, pk):

	tasks = Task.objects.get(id=pk)

	context={
		'tasks' : tasks,
		}

	return render(request, 'ttt/view_task.html', context)


def create_task(request):

	AllocateTaskFormset = inlineformset_factory(Member, Task, fields = ('name',))
	formset = AllocateTaskFormset()
	if request.method == 'POST':
		if formset.is_valid():
			formset.save()
			return redirect('/')

	return render(request, 'ttt/create_task.html', {'formset' : formset})



def update_task(request, pk):

	task_details = Task.objects.get(id=pk)
	task_name = task_details.name
	member_name = task_details.member.name
	form = TaskUpdateForm(instance=task_details)
	
	if request.method == 'POST':
		form = TaskUpdateForm(request.POST, instance=task_details)
		if form.is_valid():
			form.save()
			return redirect('/')


	context={
		'form' : form,
		'task_name' : task_name,
		'member_name' : member_name
		}

	return render(request, 'ttt/update_task.html', context)



def delete_task(request, pk):

	task_details = Task.objects.get(id=pk)
	task_name = task_details.name
	member_name = task_details.member.name

	if request.method == 'POST':
		task_details.delete()
		return redirect('/')


	context={
		'task_name' : task_name,
		'member_name' : member_name,
		'task_details' : task_details
		}

	return render(request, 'ttt/delete_task.html', context)
