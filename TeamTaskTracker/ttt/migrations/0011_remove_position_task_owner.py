# Generated by Django 3.1.7 on 2021-05-28 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0010_auto_20210528_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='task_owner',
        ),
    ]
