# Generated by Django 2.2.4 on 2019-08-30 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gp', '0003_auto_20190830_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='highlight',
            options={'ordering': ['city', 'genre', 'highlight_type', 'order_priority'], 'verbose_name': 'Highlight', 'verbose_name_plural': 'Highlights'},
        ),
    ]
