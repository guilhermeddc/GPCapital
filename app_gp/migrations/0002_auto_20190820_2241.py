# Generated by Django 2.2.4 on 2019-08-21 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicescity',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True, verbose_name='slug'),
            preserve_default=False,
        ),
    ]
