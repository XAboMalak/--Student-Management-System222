# Generated by Django 4.1.4 on 2023-01-22 10:20

import datetime
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
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='إسم الموظف')),
                ('salary', models.IntegerField(verbose_name='الراتب')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='إسم نوع العمل')),
                ('m3_day', models.FloatField(verbose_name='كمية الانجاز في اليوم')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=100, unique=True, verbose_name='إسم الوظيفة')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='الكمية')),
                ('unit', models.CharField(choices=[('1', 'متر مكعب'), ('2', 'طابوقة'), ('3', 'متر مربع'), ('4', 'متر طولي')], max_length=1, verbose_name='الوحدة')),
                ('start_Date', models.DateField(default=datetime.date.today, verbose_name='تاريخ البداية')),
                ('finish_Date', models.DateField(default=datetime.date.today, verbose_name='تاريخ الانتهاء')),
                ('number_Of_Days', models.IntegerField(verbose_name='عدد الايام')),
                ('number_Of_Hours', models.IntegerField(verbose_name='عدد الساعات')),
                ('nots', models.TextField(blank=True, null=True, verbose_name='ملاحظات')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('is_mission_close', models.BooleanField(default=False, verbose_name='الحالة')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_Job_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studens.job_type', verbose_name='نوع العمل')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='إسم المشروع')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='تاريخ الاستلام')),
                ('nots', models.TextField(blank=True, null=True, verbose_name='ملاحظات')),
            ],
        ),
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='إسم المرحلة')),
            ],
        ),
        migrations.CreateModel(
            name='MissionTimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='التاريخ')),
                ('employee', models.ManyToManyField(to='studens.employee', verbose_name='إسم الموظفين')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studens.mission', verbose_name='إسم المهمة')),
            ],
        ),
        migrations.AddField(
            model_name='mission',
            name='project_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studens.projects', verbose_name='إسم المشروع'),
        ),
        migrations.AddField(
            model_name='mission',
            name='stages',
            field=models.ManyToManyField(to='studens.stages', verbose_name='المرحلة'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studens.jobs', verbose_name='إسم الوظيفة'),
        ),
    ]
