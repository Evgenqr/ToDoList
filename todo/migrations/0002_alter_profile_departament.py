# Generated by Django 3.2.9 on 2022-10-27 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='departament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.departament', verbose_name='Отдел'),
        ),
    ]