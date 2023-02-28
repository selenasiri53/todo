from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView):  # built in Django: ListAPIView
    queryset = Todo.objects.all()  # make a request for all objects
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):  # Retrieve a single API View
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
