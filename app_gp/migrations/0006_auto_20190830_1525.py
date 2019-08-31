# Generated by Django 2.2.4 on 2019-08-30 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_gp', '0005_auto_20190830_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='client',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='app_gp.Client'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='highlight',
            name='url',
            field=models.CharField(blank=True, default=1, max_length=255),
            preserve_default=False,
        ),
    ]
