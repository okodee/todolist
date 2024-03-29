
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),  # Include URL patterns from the todo app
]
