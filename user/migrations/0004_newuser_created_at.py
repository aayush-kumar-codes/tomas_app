# Generated by Django 3.2.9 on 2022-01-08 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220108_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
