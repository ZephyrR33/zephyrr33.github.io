from html.entities import name2codepoint
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('genres', views.genres, name='genres'),
    path('favorites', views.favorites, name='favorites'),
    path('premium', views.premium, name='premium'),
    path('ganres_week', views.ganres_week, name='ganres_week'),
    path('ganers_month', views.ganers_month, name='ganers_month'),
    
    
]
