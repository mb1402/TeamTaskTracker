# Generated by Django 3.1.7 on 2021-05-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0004_auto_20210528_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('developer', 'Developer'), ('tester', 'Tester'), ('support', 'Support')], max_length=100, null=True),
        ),
    ]