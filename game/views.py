from django.shortcuts import render
from .models import Game, Developer, Genre, Platform, Mode
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
 
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            return redirect('/accounts/login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def game_list(request):
    all_games = Game.objects.all().order_by('-release_date')
    paginator = Paginator(all_games, 15)

    page = request.GET.get('page')
    games = paginator.get_page(page)

    if 'search' in request.GET:
        search_term = request.GET['search']
        games = all_games.filter(Q(name__contains=search_term))
        
    return render(request, 'game/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    platforms = game.platforms.all()

    return render(request, 'game/game_detail.html', {'game': game, 'platforms': platforms})