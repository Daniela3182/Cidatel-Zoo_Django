from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_menu, name='game_menu'),
    path('start/', views.start_game, name='start_game'),
    path('play/<int:session_id>/<int:q_index>/', views.play, name='play'),
    path('result/<int:session_id>/', views.result, name='result'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
]
