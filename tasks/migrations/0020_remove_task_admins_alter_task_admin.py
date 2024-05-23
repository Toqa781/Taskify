# Generated by Django 5.0.6 on 2024-05-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_task_admins_alter_task_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='admins',
        ),
        migrations.AlterField(
            model_name='task',
            name='admin',
            field=models.CharField(max_length=15, null=True),
        ),
    ]