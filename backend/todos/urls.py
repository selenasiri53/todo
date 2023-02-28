from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),  # primary key
    path('', ListTodo.as_view()),
]
