# Generated by Django 3.1.7 on 2021-05-29 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0015_remove_member_task_assigned'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('task_status', models.CharField(choices=[('Not Yet Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='member',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='TaskStatus',
        ),
        migrations.AddField(
            model_name='allocation',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ttt.member'),
        ),
        migrations.AddField(
            model_name='allocation',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ttt.task'),
        ),
    ]
