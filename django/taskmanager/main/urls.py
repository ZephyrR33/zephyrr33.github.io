from html.entities import name2codepoint
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.index, name='index'),
    path('genres', views.Genre.genres, name='genres'),
    path('favorites', views.favorites, name='favorites'),
    path('premium', views.premium, name='premium'),
    path('genres_week', views.genres_week, name='genres_week'),
    path('genres_mounth', views.genres_mounth, name='genres_mounth'),
    #
    #anime main pages
    #
    # path('dororo', views.dororo_main, name='dororo_main'),
    # path('homeless-god', views.homeless_god_main, name='homeless_god_main'),
    # path('tower-of-god', views.tower_of_god_main, name='tower_of_god_main'),
    # path('onepunchman', views.onepunchman_main, name='onepunchman_main'),
    # path('tokyo-avengers', views.tokyo_avengers_main, name='tokyo_avengers_main'),
    #
    #new anime pages
    #
    path('onepunchman', views.opm1_1, name='onepunchman'),
    path('homeless-god', views.hg1_1, name='homeless_god'),
    path('dororo', views.dor1, name='dororo'),
    # path('tower-of-god', views.tog1, name='tower_of_god'),
    path('tokyo-avengers', views.ta1, name='tokyo_avengers'),
    path('<slug:slug>/', views.AnimeDetail.as_view(), name='page_anime'),
    # path('search/', views.Search.as_view(), name='search'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('index-twice', views.indextwicee, name='qwe')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    #
    #onepunchman season 1
    #
    
    path('onepunchman/season-1/episode-2', views.opm2_1, name='onepunchman_season_1_episode_2'),
    path('onepunchman/season-1/episode-3', views.opm3_1, name='onepunchman_season_1_episode_3'),
    path('onepunchman/season-1/episode-4', views.opm4_1, name='onepunchman_season_1_episode_4'),
    path('onepunchman/season-1/episode-5', views.opm5_1, name='onepunchman_season_1_episode_5'),
    path('onepunchman/season-1/episode-6', views.opm6_1, name='onepunchman_season_1_episode_6'),
    path('onepunchman/season-1/episode-7', views.opm7_1, name='onepunchman_season_1_episode_7'),
    path('onepunchman/season-1/episode-8', views.opm8_1, name='onepunchman_season_1_episode_8'),
    path('onepunchman/season-1/episode-9', views.opm9_1, name='onepunchman_season_1_episode_9'),
    path('onepunchman/season-1/episode-10', views.opm10_1, name='onepunchman_season_1_episode_10'),
    path('onepunchman/season-1/episode-11', views.opm11_1, name='onepunchman_season_1_episode_11'),
    path('onepunchman/season-1/episode-12', views.opm12_1, name='onepunchman_season_1_episode_12'),
    #
    #onepunchman season 2
    #
    path('onepunchman/season-2/episode-1', views.opm1_2, name='onepunchman_season_2_episode_1'),
    path('onepunchman/season-2/episode-2', views.opm2_2, name='onepunchman_season_2_episode_2'),
    path('onepunchman/season-2/episode-3', views.opm3_2, name='onepunchman_season_2_episode_3'),
    path('onepunchman/season-2/episode-4', views.opm4_2, name='onepunchman_season_2_episode_4'),
    path('onepunchman/season-2/episode-5', views.opm5_2, name='onepunchman_season_2_episode_5'),
    path('onepunchman/season-2/episode-6', views.opm6_2, name='onepunchman_season_2_episode_6'),
    path('onepunchman/season-2/episode-7', views.opm7_2, name='onepunchman_season_2_episode_7'),
    path('onepunchman/season-2/episode-8', views.opm8_2, name='onepunchman_season_2_episode_8'),
    path('onepunchman/season-2/episode-9', views.opm9_2, name='onepunchman_season_2_episode_9'),
    path('onepunchman/season-2/episode-10', views.opm10_2, name='onepunchman_season_2_episode_10'),
    path('onepunchman/season-2/episode-11', views.opm11_2, name='onepunchman_season_2_episode_11'),
    path('onepunchman/season-2/episode-12', views.opm12_2, name='onepunchman_season_2_episode_12'),
    
    #
    #homeless god season 1
    #
    
    path('homeless-god/season-1/episode-2', views.hg2_1, name='homeless_god_season_1_episode_2'),
    path('homeless-god/season-1/episode-3', views.hg3_1, name='homeless_god_season_1_episode_3'),
    path('homeless-god/season-1/episode-4', views.hg4_1, name='homeless_god_season_1_episode_4'),
    path('homeless-god/season-1/episode-5', views.hg5_1, name='homeless_god_season_1_episode_5'),
    path('homeless-god/season-1/episode-6', views.hg6_1, name='homeless_god_season_1_episode_6'),
    path('homeless-god/season-1/episode-7', views.hg7_1, name='homeless_god_season_1_episode_7'),
    path('homeless-god/season-1/episode-8', views.hg8_1, name='homeless_god_season_1_episode_8'),
    path('homeless-god/season-1/episode-9', views.hg9_1, name='homeless_god_season_1_episode_9'),
    path('homeless-god/season-1/episode-10', views.hg10_1, name='homeless_god_season_1_episode_10'),
    path('homeless-god/season-1/episode-11', views.hg11_1, name='homeless_god_season_1_episode_11'),
    path('homeless-god/season-1/episode-12', views.hg12_1, name='homeless_god_season_1_episode_12'),
    #
    #homeless god season 2
    #
    path('homeless-god/season-2/episode-1', views.hg1_2, name='homeless_god_season_2_episode_1'),
    path('homeless-god/season-2/episode-2', views.hg2_2, name='homeless_god_season_2_episode_2'),
    path('homeless-god/season-2/episode-3', views.hg3_2, name='homeless_god_season_2_episode_3'),
    path('homeless-god/season-2/episode-4', views.hg4_2, name='homeless_god_season_2_episode_4'),
    path('homeless-god/season-2/episode-5', views.hg5_2, name='homeless_god_season_2_episode_5'),
    path('homeless-god/season-2/episode-6', views.hg6_2, name='homeless_god_season_2_episode_6'),
    path('homeless-god/season-2/episode-7', views.hg7_2, name='homeless_god_season_2_episode_7'),
    path('homeless-god/season-2/episode-8', views.hg8_2, name='homeless_god_season_2_episode_8'),
    path('homeless-god/season-2/episode-9', views.hg9_2, name='homeless_god_season_2_episode_9'),
    path('homeless-god/season-2/episode-10', views.hg10_2, name='homeless_god_season_2_episode_10'),
    path('homeless-god/season-2/episode-11', views.hg11_2, name='homeless_god_season_2_episode_11'),
    path('homeless-god/season-2/episode-12', views.hg12_2, name='homeless_god_season_2_episode_12'),
    path('homeless-god/season-2/episode-13', views.hg13_2, name='homeless_god_season_2_episode_13'),
    #
    #dororo
    #
    
    path('dororo/episode-2', views.dor2, name='dororo_episode_2'),
    path('dororo/episode-3', views.dor3, name='dororo_episode_3'),
    path('dororo/episode-4', views.dor4, name='dororo_episode_4'),
    path('dororo/episode-5', views.dor5, name='dororo_episode_5'),
    path('dororo/episode-6', views.dor6, name='dororo_episode_6'),
    path('dororo/episode-7', views.dor7, name='dororo_episode_7'),
    path('dororo/episode-8', views.dor8, name='dororo_episode_8'),
    path('dororo/episode-9', views.dor9, name='dororo_episode_9'),
    path('dororo/episode-10', views.dor10, name='dororo_episode_10'),
    path('dororo/episode-11', views.dor11, name='dororo_episode_11'),
    path('dororo/episode-12', views.dor12, name='dororo_episode_12'),
    path('dororo/episode-13', views.dor13, name='dororo_episode_13'),
    path('dororo/episode-14', views.dor14, name='dororo_episode_14'),
    path('dororo/episode-15', views.dor15, name='dororo_episode_15'),
    path('dororo/episode-16', views.dor16, name='dororo_episode_16'),
    path('dororo/episode-17', views.dor17, name='dororo_episode_17'),
    path('dororo/episode-18', views.dor18, name='dororo_episode_18'),
    path('dororo/episode-19', views.dor19, name='dororo_episode_19'),
    path('dororo/episode-20', views.dor20, name='dororo_episode_20'),
    path('dororo/episode-21', views.dor21, name='dororo_episode_21'),
    path('dororo/episode-22', views.dor22, name='dororo_episode_22'),
    path('dororo/episode-23', views.dor23, name='dororo_episode_23'),
    path('dororo/episode-24', views.dor24, name='dororo_episode_24'),
    #
    #tower of god
    #
    
    path('tower-of-god/episode-2', views.tog2, name='tower_of_god_episode_2'),
    path('tower-of-god/episode-3', views.tog3, name='tower_of_god_episode_3'),
    path('tower-of-god/episode-4', views.tog4, name='tower_of_god_episode_4'),
    path('tower-of-god/episode-5', views.tog5, name='tower_of_god_episode_5'),
    path('tower-of-god/episode-6', views.tog6, name='tower_of_god_episode_6'),
    path('tower-of-god/episode-7', views.tog7, name='tower_of_god_episode_7'),
    path('tower-of-god/episode-8', views.tog8, name='tower_of_god_episode_8'),
    path('tower-of-god/episode-9', views.tog9, name='tower_of_god_episode_9'),
    path('tower-of-god/episode-10', views.tog10, name='tower_of_god_episode_10'),
    path('tower-of-god/episode-11', views.tog11, name='tower_of_god_episode_11'),
    path('tower-of-god/episode-12', views.tog12, name='tower_of_god_episode_12'),
    path('tower-of-god/episode-13', views.tog13, name='tower_of_god_episode_13'),
    #
    #tokyo avengers
    #
    
    path('tokyo-avengers/episode-2', views.ta2, name='tokyo_avengers_episode_2'),
    path('tokyo-avengers/episode-3', views.ta3, name='tokyo_avengers_episode_3'),
    path('tokyo-avengers/episode-4', views.ta4, name='tokyo_avengers_episode_4'),
    path('tokyo-avengers/episode-5', views.ta5, name='tokyo_avengers_episode_5'),
    path('tokyo-avengers/episode-6', views.ta6, name='tokyo_avengers_episode_6'),
    path('tokyo-avengers/episode-7', views.ta7, name='tokyo_avengers_episode_7'),
    path('tokyo-avengers/episode-8', views.ta8, name='tokyo_avengers_episode_8'),
    path('tokyo-avengers/episode-9', views.ta9, name='tokyo_avengers_episode_9'),
    path('tokyo-avengers/episode-10', views.ta10, name='tokyo_avengers_episode_10'),
    path('tokyo-avengers/episode-11', views.ta11, name='tokyo_avengers_episode_11'),
    path('tokyo-avengers/episode-12', views.ta12, name='tokyo_avengers_episode_12'),
    path('tokyo-avengers/episode-13', views.ta13, name='tokyo_avengers_episode_13'),
    path('tokyo-avengers/episode-14', views.ta14, name='tokyo_avengers_episode_14'),
    path('tokyo-avengers/episode-15', views.ta15, name='tokyo_avengers_episode_15'),
    path('tokyo-avengers/episode-16', views.ta16, name='tokyo_avengers_episode_16'),
    path('tokyo-avengers/episode-17', views.ta17, name='tokyo_avengers_episode_17'),
    path('tokyo-avengers/episode-18', views.ta18, name='tokyo_avengers_episode_18'),
    path('tokyo-avengers/episode-19', views.ta19, name='tokyo_avengers_episode_19'),
    path('tokyo-avengers/episode-20', views.ta20, name='tokyo_avengers_episode_20'),
    path('tokyo-avengers/episode-21', views.ta21, name='tokyo_avengers_episode_21'),
    path('tokyo-avengers/episode-22', views.ta22, name='tokyo_avengers_episode_22'),
    path('tokyo-avengers/episode-23', views.ta23, name='tokyo_avengers_episode_23'),
    path('tokyo-avengers/episode-24', views.ta24, name='tokyo_avengers_episode_24'),
'''