from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Departament(models.Model):
    title = models.CharField(max_length=250, verbose_name="Отдел")
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.title


class Profile(AbstractUser):
    username = models.CharField(max_length=50, unique=True,
                                verbose_name="Имя пользователя")
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    departament = models.ForeignKey(Departament, verbose_name="Отдел",
                                    on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Stage(models.Model):
    title = models.CharField(max_length=250, verbose_name="Стадия исполнения")
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name = "Стадия"
        verbose_name_plural = "Стадии"

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    text = models.TextField(verbose_name="Текст задания")
    stage = models.ForeignKey(Stage, verbose_name="Стадия выполнения",
                              on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Комментарий",
                               blank=True, null=True)
    date_add = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания задания")
    deadline = models.DateTimeField(verbose_name="Срок выполнения")
    date_end = models.DateTimeField(null=True, verbose_name="Дата выполнения")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.title
