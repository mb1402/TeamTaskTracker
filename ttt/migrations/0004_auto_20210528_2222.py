# Generated by Django 3.1.7 on 2021-05-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0003_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='birthday',
        ),
        migrations.AddField(
            model_name='member',
            name='dob',
            field=models.DateField(max_length=8, null=True),
        ),
    ]