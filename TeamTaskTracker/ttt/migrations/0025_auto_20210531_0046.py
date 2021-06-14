# Generated by Django 3.1.7 on 2021-05-30 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0024_auto_20210530_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ttt.member'),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='task',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ttt.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ttt.member'),
        ),
    ]