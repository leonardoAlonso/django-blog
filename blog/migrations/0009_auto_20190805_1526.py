# Generated by Django 2.2.4 on 2019-08-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190805_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
