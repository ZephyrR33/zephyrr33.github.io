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
    res1080 = models.CharField('res1080', max_length=250)
    res720 = models.CharField('res720', max_length=250)
    res480 = models.CharField('res480', max_length=250)
    res360 = models.CharField('res360', max_length=250)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'onepunchman'            #переименование (единственное число)
        verbose_name_plural = 'onepunchmen'     #переименование (множественное число)

