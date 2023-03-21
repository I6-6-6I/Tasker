from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('edit/<int:task_id>/', views.edit, name="edit"),
    path('updatetaskdata/<int:task_id>', views.updatetaskdata, name="updatetaskdata"),
    path('addworker', views.addworker, name="addworker"),
    path('deleteworker/<int:worker_id>/', views.deleteworker, name="deleteworker"),
    path('update/<int:task_id>/', views.update, name="update"),
    path('delete/<int:task_id>/', views.delete, name="delete"),
]