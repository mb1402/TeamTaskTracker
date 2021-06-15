from django.shortcuts import render, redirect
from django.forms import inlineformset_factory, formset_factory
from django.http import HttpResponse


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import TaskCreateForm, TaskUpdateForm, CreateUserForm, TaskAllocateForm
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.




@unauthenticated_user
def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			group = Group.objects.get(name='member')
			user.groups.add(group)

			Member.objects.create(
				user=user,
				name=user.username,
				)

			
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')

	context = {'form':form}
	return render(request, 'ttt/register.html', context)




@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Incorrect Username/Password')
			return render(request, 'ttt/login.html')


	return render(request, 'ttt/login.html')




def logoutPage(request):
	logout(request)
	return render(request, 'ttt/logout.html')




@login_required(login_url='login')
@admin_only
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




@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def user_profile(request):

	user = Member.objects.get(name=request.user)
	user_task = Allocation.objects.filter(member__name=user)


	total_tasks = user_task.count()
	tasks_pending = user_task.filter(task__task_status='In Progress')
	task_pending_count = tasks_pending.count()
	tasks_completed = user_task.filter(task__task_status='Completed').count()


	context = {
	'user':user,
	'user_task':user_task,
	'total_tasks':total_tasks,
	'task_pending_count':task_pending_count,
	'tasks_completed':tasks_completed

	}

	return render(request, 'ttt/user.html', context)



@login_required(login_url='login')
@admin_only
def members(request):
	members = Member.objects.all()

	context = {
		'members':members,
	}

	return render(request, 'ttt/members.html', context)



@login_required(login_url='login')
@admin_only
def tasks(request):
	tasks = Task.objects.all()

	context = {
		'tasks':tasks,
	}

	return render(request, 'ttt/tasks.html', context)



# @login_required(login_url='login')
# def member(request, pk_test):
# 	members = Member.objects.get(id=pk_test)
# 	task_details = Allocation.objects.filter(member__id=pk_test)


# 	task_count = task_details.count()

# 	context = {
# 		'members':members,
# 		'task_details' : task_details,
# 		'task_count':task_count

# 	}

# 	return render(request, 'ttt/member.html', context)




@login_required(login_url='login')
def view_task(request, pk):

	tasks = Task.objects.get(id=pk)

	context={
		'tasks' : tasks,
		}

	return render(request, 'ttt/view_task.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_task(request):
	form = TaskCreateForm()
	if request.method == 'POST':
		form = TaskCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('tasks')

	context = {
	'form':form
	}


	return render(request, 'ttt/create_task.html', {'form' : form})



@login_required(login_url='login')
def allocate_task(request, pk):

	task_details = Task.objects.get(id=pk)
	unallocated_tasks = Allocation.objects.filter(member__isnull=True)
	print(unallocated_tasks)
	for u in unallocated_tasks:
		print('value', task_details.allocation__set.add(u))
	form = TaskAllocateForm(instance=task_details)
	if request.method == 'POST':
		form = TaskAllocateForm(request.POST, instance=task_details)
		if form.is_valid():
			form.save()
			return redirect('/')
	# try:
	# 	unallocated_tasks = Task.objects.filter(member__isnull=True)
	# except Task.DoesNotExist:
	# 	unallocated_tasks = None

	# if unallocated_tasks == None:
	# 	return redirect('error')
	# else:
	# 	form = TaskAllocateForm(instance=unallocated_tasks)

	# 	if request.method == 'POST':
	# 		form = TaskAllocateForm(request.POST, instance=unallocated_tasks)
	# 		if form.is_valid():
	# 			form.save()
	# 			return redirect('/')


	context = {
		'form':form,
		}


	return render(request, 'ttt/allocate_task.html', context)





@login_required(login_url='login')
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


def error(request):
	return render(request, 'ttt/error.html')