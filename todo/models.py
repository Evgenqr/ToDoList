from ast import Delete
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


class Departament(models.Model):
    title = models.CharField(max_length=250, verbose_name="Отдел")

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plular = "Отделы"

    def __str__(self):
        return self.title


class Profile(AbstractUser):
    departament = models.ForeignKey(Departament, verbose_name="Отдел",
                                    delete=models.CASCADE)


class Stage(models.Model):
    title = models.CharField(max_length=250, verbose_name="Стадия исполнения")

    class Meta:
        verbose_name = "Стадия"
        verbose_name_plular = "Стадии"

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=250, verbose_name="Задание")
    user - models.ForeignKey(Profile, verbose_name="Пользователь",
                             delete=models.CASCADE)
    comment = models.TextField(verbose_name="Комментарий",
                               blank=True, null=True)
    date_add = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания задания")
    deadline = models.DateTimeField(verbose_name="Срок выполнения")
    date_end = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата выполнения")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plular = "Задания"

    def __str__(self):
        return self.title
