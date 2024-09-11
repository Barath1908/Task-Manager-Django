from django.urls import path
from .views import *

urlpatterns = [
  path('', home_view, name='home'),
  path('add/', add_task, name='add_task'),
  path('edit/<uuid:task_id>/', edit_task, name='edit_task'),
  path('delete/<uuid:task_id>/', delete_task, name='delete_task'),
]