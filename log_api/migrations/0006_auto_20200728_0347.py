# Generated by Django 3.0.8 on 2020-07-28 06:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_api', '0005_auto_20200720_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('environment', models.CharField(choices=[('DEV', 'Development'), ('PROD', 'Production'), ('QA', 'Quality Assurance'), ('TEST', 'Test')], default='DEV', max_length=30, verbose_name='Enviroment')),
                ('address', models.GenericIPAddressField(null=True, protocol='IPV4', validators=[django.core.validators.validate_ipv4_address])),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='execution_id',
        ),
        migrations.RemoveField(
            model_name='execution',
            name='environment',
        ),
        migrations.AddField(
            model_name='event',
            name='execution',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='related_execution', to='log_api.Execution'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='execution',
            name='application_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='application_execution', to='log_api.Application'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='execution',
            name='machine_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='machine_execution', to='log_api.Machine'),
            preserve_default=False,
        ),
    ]