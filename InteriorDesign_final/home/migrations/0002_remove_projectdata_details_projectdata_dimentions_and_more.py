# Generated by Django 5.1.1 on 2024-09-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdata',
            name='details',
        ),
        migrations.AddField(
            model_name='projectdata',
            name='Dimentions',
            field=models.TextField(default='Default Dimentions'),
        ),
        migrations.AddField(
            model_name='projectdata',
            name='FurnitureHighlights',
            field=models.TextField(default='Standard Furniture'),
        ),
        migrations.AddField(
            model_name='projectdata',
            name='RoomHighlights',
            field=models.TextField(default='Standard Room'),
        ),
    ]
