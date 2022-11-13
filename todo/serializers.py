from rest_framework import serializers
from .models import Task
from todolist import settings


# class TaskModel:

#     def __init__(self, title, text, user_id, stage_id, date_add, deadline,
#                  date_end):
#         self.title = title
#         self.text = text
#         self.user_id = user_id
#         self.stage_id = stage_id
#         self.date_add = date_add
#         self.deadline = deadline
#         self.date_end = date_end


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    user_id = serializers.IntegerField()
    stage_id = serializers.IntegerField()
    date_add = serializers.DateTimeField(read_only=True,
                                         format=settings.DATE_FORMAT)
    deadline = serializers.DateTimeField(format=settings.DATE_FORMAT)
    date_end = serializers.DateTimeField(format=settings.DATE_FORMAT)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.stage_id = validated_data.get('stage_id', instance.stage_id)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.save()
        return instance
