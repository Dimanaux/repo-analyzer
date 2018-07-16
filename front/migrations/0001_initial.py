# Generated by Django 2.0.7 on 2018-07-16 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('time_from', models.DateTimeField()),
                ('time_to', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('time_from', models.DateTimeField()),
                ('time_to', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.TaskSet'),
        ),
    ]