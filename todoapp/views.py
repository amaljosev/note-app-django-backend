from django.shortcuts import render, redirect
from .models import Todos
from .serializer import TodosSerializer
from rest_framework import viewsets


# Create your views here.
class Todos(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer