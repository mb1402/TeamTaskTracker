from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Member(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	DESIGNATION = [
		('Developer', 'Developer'),
		('Tester', 'Tester'),
		('Support', 'Support'),
		]
	name = models.CharField(max_length=200, null=True)
	role = models.CharField(max_length=100, null=True, choices=DESIGNATION)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name



class Task(models.Model):
	CATEGORY = [
		( 'Low', 'Low'),
		('Medium', 'Medium'),
		('Urgent', 'Urgent'),
		]

	STATUS = [
		('Not Started', 'Not Started'),
		('In Progress', 'In Progress'),
		('Completed', 'Completed'),
		]
	
	name = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	member = models.ForeignKey('Member', null=True, on_delete=models.CASCADE)
	task_status = models.CharField(max_length=200, null=True, choices=STATUS)



	def __str__(self):
		return self.name




class Allocation(models.Model):
	
	member = models.ForeignKey('Member', null=True, on_delete=models.CASCADE)
	task = models.OneToOneField('Task', null=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.task.name










