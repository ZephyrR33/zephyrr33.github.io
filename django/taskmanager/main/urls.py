from html.entities import name2codepoint
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('', views.index_css),
    path('genres', views.genres, name='genres'),
    path('favorites', views.favorites, name='favorites'),
    path('premium', views.premium, name='premium'),
    
    
]
