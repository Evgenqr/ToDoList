from django.contrib import admin
from .models import Task, Stage, Profile, Departament


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'comment', 'user', 'date_add', 'deadline', 'date_end'
        ]
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'comment', 'user', 'date_add', 'deadline', 'date_end'
        ]
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'comment', 'user', 'date_add', 'deadline', 'date_end'
        ]
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'comment', 'user', 'date_add', 'deadline', 'date_end'
        ]
