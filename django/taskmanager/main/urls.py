from html.entities import name2codepoint
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('genres', views.genres, name='genres'),
    path('favorites', views.favorites, name='favorites'),
    path('premium', views.premium, name='premium'),
    path('genres_week', views.genres_week, name='genres_week'),
    path('genres_mounth', views.genres_mounth, name='genres_mounth'),
    
    
]
