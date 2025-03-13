from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/update/<int:task_id>/', views.update_task, name='update_task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
