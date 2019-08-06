# Generated by Django 2.2.4 on 2019-08-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190805_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='categorias',
        ),
        migrations.AddField(
            model_name='articulo',
            name='categorias',
            field=models.ManyToManyField(to='blog.Categoria'),
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='tags',
        ),
        migrations.AddField(
            model_name='articulo',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
