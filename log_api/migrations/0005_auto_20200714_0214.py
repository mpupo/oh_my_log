# Generated by Django 3.0.8 on 2020-07-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_api', '0004_auto_20200714_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='archived',
            field=models.BooleanField(verbose_name='Archived'),
        ),
        migrations.AlterField(
            model_name='event',
            name='dateref',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
