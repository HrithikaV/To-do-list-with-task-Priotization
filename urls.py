from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
]
