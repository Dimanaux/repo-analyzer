# Generated by Django 2.0.7 on 2018-07-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskset',
            name='time_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskset',
            name='time_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]