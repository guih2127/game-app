from django.shortcuts import render
from .models import Game, Developer, Genre, Platform, Mode, UserGamesInformation, Review, User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, ReviewForm
 
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

@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_reviews = Review.objects.filter(author=user)
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    wishlist = user_games.want_to_play.order_by()[0:5]
    currently_playing = user_games.currently_playing.order_by()[0:5]
    finished = user_games.finished.order_by()[0:5]

    return render(request, 'game/profile.html', {'user_reviews': user_reviews,
    'user_games': user_games, 'wishlist': wishlist, 'currently_playing': currently_playing,
    'finished': finished})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    user_games = UserGamesInformation.objects.get(pk=user.id)
    wishlist = user_games.want_to_play.order_by()
    currently_playing = user_games.currently_playing.order_by()
    finished = user_games.finished.order_by()
    platforms = game.platforms.all()
    reviews = Review.objects.filter(game=pk).order_by('-date')
    reviewuser = Review.objects.filter(author=user.id, game=game.id)

    return render(request, 'game/game_detail.html', {'game': game, 'platforms': platforms,
    'reviews': reviews, 'reviewuser': reviewuser, 'finished': finished, 'wishlist': wishlist,
    'currently_playing': currently_playing})


@login_required
def add_game_to_wishlist(request, pk):
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    wishlist = user_games.want_to_play
    error = None

    if game in wishlist.all():
        error = '''Esse jogo já está na sua lista de desejados!'''
    else:
        wishlist.add(game)

    return render(request, 'game/confirmation.html', { 'error': error })

@login_required
def delete_game_from_wishlist(request, pk):
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    wishlist = user_games.want_to_play
    error = None

    if game in wishlist.all():
        wishlist.remove(game)
    else:
        error = '''Esse jogo não está na sua lista de desejados!'''

    return render(request, 'game/confirmation_delete.html', { 'error': error })

@login_required
def add_game_to_currently_playing(request, pk):
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    currently_playing = user_games.currently_playing
    error = None

    if game in currently_playing.all():
        error = '''Você já adicionou esse jogo na sua lista atual!'''
    else:
        currently_playing.add(game)

    return render(request, 'game/confirmation.html', { 'error': error })

@login_required
def delete_game_from_currently_playing(request, pk):
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    currently_playing = user_games.currently_playing
    error = None

    if game in currently_playing.all():
        currently_playing.remove(game)
    else:
        error = '''Esse jogo não está na sua lista atual!'''

    return render(request, 'game/confirmation_delete.html', { 'error': error })

@login_required
def add_game_to_finished(request, pk):
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    finished = user_games.finished
    error = None

    if game in finished.all():
        error = '''Você já adicionou esse jogo na sua lista de finalizados!'''
    else:
        finished.add(game)

    return render(request, 'game/confirmation.html', { 'error': error })

@login_required
def delete_game_from_finished(request, pk):
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    finished = user_games.finished
    error = None

    if game in finished.all():
        finished.remove(game)
    else:
        error = '''Esse jogo não está na sua lista de finalizados!'''

    return render(request, 'game/confirmation_delete.html', { 'error': error })
    
  
@login_required
def new_review(request, pk):
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.game = Game(pk=pk)
            review.save()
            return redirect('game_detail', pk=pk)
        else:
            form = ReviewForm()
    
    return render(request, 'game/new_review.html', {'form': form, 'game': game})

@login_required
def delete_review(request, pk):
    error = None
    game = get_object_or_404(Game, pk=pk)
    user = request.user
    review = Review.objects.filter(author=user.id, game=pk)

    try:
        review.delete()
    except:
        error = 'Não foi possível apagar o seu review.'
    
    return render(request, 'game/review_deleted.html', {'review': review, 'error': error })

@login_required
def finished_list(request):
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    finished_list = user_games.finished.all()

    return render(request, 'game/finished_list.html', {'finished_list': finished_list})

@login_required
def wishlist(request):
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    wishlist = user_games.want_to_play.all()

    return render(request, 'game/wishlist.html', {'wishlist': wishlist})

@login_required
def playing_list(request):
    user = request.user
    user_games = UserGamesInformation.objects.get_or_create(pk=user.id)
    user_games = UserGamesInformation.objects.get(pk=user.id)
    playing_list = user_games.currently_playing.all()

    return render(request, 'game/playing_list.html', {'playing_list': playing_list})
