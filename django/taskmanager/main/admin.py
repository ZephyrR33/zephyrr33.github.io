from django.contrib import admin
from .models import Genre, Anime, Rating, Ratingstar
# Register your models here.


admin.site.register(Genre)
admin.site.register(Anime)
admin.site.register(Rating)
admin.site.register(Ratingstar)

