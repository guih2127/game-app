from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:pk>', views.game_detail, name='game_detail'),
    path('playing/<int:pk>', views.add_game_to_currently_playing, name='playing'),
    path('wishlist/<int:pk>', views.add_game_to_wishlist, name='wishlist'),
    path('finished/<int:pk>', views.add_game_to_finished, name='finished'),
    path('delete_playing/<int:pk>', views.delete_game_from_currently_playing, name='delete_playing'),
    path('delete_wishlist/<int:pk>', views.delete_game_from_wishlist, name='delete_wishlist'),
    path('delete_finished/<int:pk>', views.delete_game_from_finished, name='delete_finished'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('new_review/<int:pk>', views.new_review, name='new_review'),
    path('delete_review/<int:pk>', views.delete_review, name='delete_review'),
    path('finished_list/', views.finished_list, name="finished_list"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('playing_list/', views.playing_list, name="playing_list"),
    path('users', views.users, name="users"),
    path('user_detail/<int:pk>', views.user_detail, name="user_detail")
]
