# Generated by Django 3.1.7 on 2021-05-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0008_member_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='task_owner',
            field=models.ManyToManyField(to='ttt.Member'),
        ),
    ]
