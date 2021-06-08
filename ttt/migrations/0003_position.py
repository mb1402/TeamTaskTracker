# Generated by Django 3.1.7 on 2021-05-28 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0002_auto_20210528_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ttt.member')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ttt.task')),
            ],
        ),
    ]