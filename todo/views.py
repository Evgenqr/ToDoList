# from django.shortcuts import render
# from rest_framework import generics
# from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer

# class TaskAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers


class TaskAPIView(APIView):
    def get(self, request):
        tsk = Task.objects.all().values()
        return Response({'tasks': TaskSerializer(tsk, many=True).data})

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # task_new = Task.objects.create(
        #     title=request.data['title'],
        #     text=request.data['text'],
        #     user_id=request.data['user_id'],
        #     stage_id=request.data['stage_id'],
        #     # date_add=request.data['date_add'],
        #     deadline=request.data['deadline'],
        #     date_end=request.data['date_end']
        # )
        return Response({'task': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Метод PUT не определен'})
        try:
            isinstance = Task.objects.get(pk=pk)
        except:
            return Response({'error': 'Объект не найден'})
        serializer = TaskSerializer(data=request.data, instance=isinstance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'task': serializer.data})
    
    def delete(self, request, *args, **kwargs):
            pk = kwargs.get('pk', None)
            if not pk:
                return Response({'error': 'Метод DELETE не определен'})
            try:
                isinstance = Task.objects.get(pk=pk)
            except:
                return Response({'error': 'Объект не найден'})
            serializer = TaskSerializer(data=request.data, instance=isinstance)
            serializer.is_valid(raise_exception=True)
            serializer.delete()
    
            return Response({'task': 'Удалена задача ' + str(pk)})

