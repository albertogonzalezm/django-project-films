# Generated by Django 4.1.7 on 2023-02-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmDirectors', '0003_film_poster_alter_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='information',
            field=models.CharField(default='SOME STRING', max_length=700),
        ),
    ]