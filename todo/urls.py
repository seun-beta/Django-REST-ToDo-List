from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoList.as_view()),
    path('<todo_id>/', views.ToDoOne.as_view()),
]