from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


from .models import *


class TaskCreateForm(ModelForm):
	class Meta:
		model = Task 
		fields = ['name', 'category', 'description', 'task_status']


class TaskUpdateForm(ModelForm):
	class Meta:
		model = Task 
		fields = ['category', 'description', 'task_status']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class TaskAllocateForm(ModelForm):
	class Meta:
		model = Task 
		fields = ['name', 'member', 'task_status']




		