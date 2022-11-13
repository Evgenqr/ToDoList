from django.contrib import admin
from .models import Task, Stage, Profile, Departament


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',  'text', 'stage', 'user',
        'date_add', 'deadline', 'date_end'
        ]


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'departament'
        ]
