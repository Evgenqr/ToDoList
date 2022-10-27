# from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializers
from .models import Task


class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
