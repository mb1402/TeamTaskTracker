from django.urls import path
from ttt import views


urlpatterns = [
	path('', views.home, name='home'),

	path('register', views.register, name='register'),
	path('login', views.loginPage, name='login'),
	path('logout', views.logoutPage, name='logout'),

	path('error', views.error, name='error'),

	path('user_profile', views.user_profile, name='user_profile'),

	path('members', views.members, name='members'),
	path('tasks', views.tasks, name='tasks'),


	path('view_task/<int:pk>/', views.view_task, name='view_task'),
	path('create_task', views.create_task, name='create_task'),
	path('allocate_task/<str:pk>/', views.allocate_task, name='allocate_task'),
	path('update_task/<str:pk>/', views.update_task, name='update_task'),
	path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),
	
]