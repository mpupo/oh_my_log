# Generated by Django 3.0.8 on 2020-07-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_api', '0002_auto_20200715_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='applications',
        ),
        migrations.CreateModel(
            name='OperationSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('version', models.CharField(max_length=8, verbose_name='Version')),
                ('installed_apps', models.ManyToManyField(to='log_api.Application')),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='operation_systems',
            field=models.ManyToManyField(to='log_api.OperationSystem'),
        ),
    ]
