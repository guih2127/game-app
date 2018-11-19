from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:pk>', views.game_detail, name='game_detail'),
    path('playing/<int:pk>', views.add_game_to_currently_playing, name='playing'),
    path('wishlist/<int:pk>', views.add_game_to_wishlist, name='wishlist'),
    path('finished/<int:pk>', views.add_game_to_finished, name='finished'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
