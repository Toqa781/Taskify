# Generated by Django 5.0.6 on 2024-05-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_alter_task_choose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]