# Generated by Django 4.0.3 on 2022-04-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='onepunchman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('sezon', models.CharField(max_length=250, verbose_name='Сезон')),
                ('episode', models.CharField(max_length=250, verbose_name='Эпизод')),
                ('res1080', models.URLField(max_length=250, verbose_name='res1080')),
                ('res720', models.URLField(max_length=250, verbose_name='res720')),
                ('res480', models.URLField(max_length=250, verbose_name='res480')),
                ('res360', models.URLField(max_length=250, verbose_name='res360')),
            ],
        ),
    ]
