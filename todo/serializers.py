from rest_framework import serializers
# from .models import Task
from todolist import settings


class TaskModel:

    def __init__(self, title, text, user_id, stage_id, date_add, deadline,
                 date_end):
        self.title = title
        self.text = text
        self.user_id = user_id
        self.stage_id = stage_id
        self.date_add = date_add
        self.deadline = deadline
        self.date_end = date_end


class TaskSerializers(serializers.Serializer):
    # print('vvddd 333 ', settings.DATE_FORMAT)
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    user_id = serializers.IntegerField()
    stage_id = serializers.IntegerField()
    date_add = serializers.DateField(format=settings.DATE_FORMAT,
                                     read_only=True)
    deadline = serializers.DateField(format=settings.DATE_FORMAT)
    date_end = serializers.DateField(format=settings.DATE_FORMAT)
