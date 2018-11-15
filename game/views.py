from django.shortcuts import render
from .models import Game, Developer, Genre, Platform, Mode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def game_list(request):
    games = Game.objects.all().order_by('-release_date')
    paginator = Paginator(games, 2)

    page = request.GET.get('page')
    games = paginator.get_page(page)
    
    return render(request, 'game/game_list.html', {'games': games})