from django.contrib import admin
from .models import Game, Developer, Genre, Platform, Mode, UserGamesInformation, Review, Friends
from .models import UserRequests

admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Mode)
admin.site.register(UserGamesInformation)
admin.site.register(Review)
admin.site.register(Friends)
admin.site.register(UserRequests)