from django.contrib import admin
from .models import Game, Developer, Genre, Platform, Mode

admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Mode)