# Generated by Django 3.1.7 on 2021-05-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0013_remove_member_task_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='task_assigned',
            field=models.ManyToManyField(to='ttt.Task'),
        ),
    ]
