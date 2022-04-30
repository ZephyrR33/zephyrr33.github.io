# Generated by Django 4.0.3 on 2022-04-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_anime_episodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='main_picture',
            field=models.ImageField(default='', upload_to='anime_posters/main_pictures/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='poster',
            field=models.ImageField(upload_to='anime_posters/anime_posters', verbose_name='Постер'),
        ),
    ]
