# Generated by Django 3.1.2 on 2020-10-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgenre',
            name='main_genre',
        ),
        migrations.AddField(
            model_name='genre',
            name='subgenres',
            field=models.ManyToManyField(to='records.SubGenre'),
        ),
    ]
