# Generated by Django 3.0 on 2019-12-20 22:13

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
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'Doing'), (3, 'Done')])),
                ('priority', models.IntegerField(choices=[(3, 'Low'), (2, 'Medium'), (1, 'High')])),
                ('task_type', models.IntegerField(choices=[(1, 'Frontend'), (2, 'Backend')])),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'Fixing'), (3, 'Fixed')])),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Task')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]