# Generated by Django 2.2.4 on 2019-08-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gp', '0003_auto_20190821_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicesgenre',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='slug'),
        ),
    ]
