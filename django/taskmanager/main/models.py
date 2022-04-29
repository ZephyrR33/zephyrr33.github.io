from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')



class onepunchman(models.Model):
    title = models.CharField('Название', max_length=250)
    sezon = models.CharField('Сезон', max_length=250)
    episode = models.CharField('Эпизод', max_length=250)
    res1080 = models.URLField('res1080', max_length=250)
    res720 = models.URLField('res720', max_length=250)
    res480 = models.URLField('res480', max_length=250)
    res360 = models.URLField('res360', max_length=250)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'onepunchman'            #переименование (единственное число)
        verbose_name_plural = 'onepunchmen'     #переименование (множественное число)



class Genre(models.Model):
    name = models.CharField('Название', max_length=250)
    url = models.SlugField(max_length=260, unique=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'            #переименование (единственное число)
        verbose_name_plural = 'Категории'     #переименование (множественное число)



class Anime(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание', default='')
    poster = models.ImageField('Постер', upload_to='anime_posters/')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    pubdate = models.DateField('Дата выхода')
    url = models.SlugField(max_length=260, unique=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Аниме'            #переименование (единственное число)
        verbose_name_plural = 'Аниме'     #переименование (множественное число)



class Ratingstar(models.Model):
    value = models.SmallIntegerField('Значение', default=0)
    

    def __str__(self):
        return self.value


    class Meta:
        verbose_name = 'Звезда рейтинга'            #переименование (единственное число)
        verbose_name_plural = 'Звезды рейтинга'     #переименование (множественное число)



class Rating(models.Model):
    ip = models.CharField('IP adress', max_length=20)
    star = models.ForeignKey(Ratingstar, on_delete=models.CASCADE, verbose_name='Звезда')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Аниме')
    

    def __str__(self):
        return f'{self.star} - {self.anime}'


    class Meta:
        verbose_name = 'Рейтинг'            #переименование (единственное число)
        verbose_name_plural = 'Рейтинги'     #переименование (множественное число)


