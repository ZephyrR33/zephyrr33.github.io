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
    path('dororo', views.dororo_main, name='dororo_main'),
    path('homeless-god', views.homeless_god_main, name='homeless_god_main'),
    path('magic-battle', views.magic_battle_main, name='magic_battle_main'),
    path('onepunchman', views.onepunchman_main, name='onepunchman_main'),
    path('the-promised-neverland', views.the_promised_neverland, name='the_promised_neverland'),
    path('the-promised-neverland/episode-1', views.tpn1, name='the_promised_neverland_episode_1'),
    
]
