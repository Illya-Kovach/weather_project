# Generated by Django 5.1.2 on 2024-11-14 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0003_remove_customuser_confirmation_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
