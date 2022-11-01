# from django.shortcuts import render
# from rest_framework import generics
from django.forms import model_to_dict
from .serializers import TaskSerializers
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response

# class TaskAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers


class TaskAPIView(APIView):
    def get(self, request):
        tsk = Task.objects.all().values()
        return Response({'tasks': list(tsk)})

    def post(self, request):
        task_new = Task.objects.create(
            title=request.data['title'],
            text=request.data['text'],
            user_id=request.data['user_id'],
            stage_id=request.data['stage_id'],
            deadline=request.data['deadline']
        )
        return Response({'task': model_to_dict(task_new)})
