from django.shortcuts import render, redirect
from .models import Todos
from .serializer import TodosSerializer
from rest_framework import generics



# Create your views here.
class TodosView(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class TodosById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
