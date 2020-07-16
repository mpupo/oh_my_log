# Generated by Django 3.0.8 on 2020-07-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='operation_systems',
        ),
        migrations.AddField(
            model_name='machine',
            name='applications',
            field=models.ManyToManyField(to='log_api.Application'),
        ),
        migrations.DeleteModel(
            name='OperationSystem',
        ),
    ]
