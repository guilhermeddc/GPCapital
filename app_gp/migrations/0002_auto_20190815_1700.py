# Generated by Django 2.2.4 on 2019-08-15 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='ClientPhoto',
        ),
        migrations.RenameModel(
            old_name='Video',
            new_name='ClientVideo',
        ),
    ]
