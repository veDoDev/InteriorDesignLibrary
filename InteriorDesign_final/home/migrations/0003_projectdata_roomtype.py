# Generated by Django 5.1 on 2024-10-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_projectdata_details_projectdata_dimentions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdata',
            name='RoomType',
            field=models.TextField(default='Uspecified'),
        ),
    ]
