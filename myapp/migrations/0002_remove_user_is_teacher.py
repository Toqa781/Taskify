# Generated by Django 5.0.6 on 2024-05-21 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
    ]