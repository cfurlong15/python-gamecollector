from django.shortcuts import render

from .models import Game

# games = [
#     {'name': 'Read Dead Redemption 2', 'release_year': ' 2018', 'rating': 'M', 'genre': 'Open World, Action-Adventure'},
#     {'name': 'Spider-Man 2', 'release_year': '2023', 'rating': 'T', 'genre': 'Open World, Action-Adventure'},
#     {'name': 'Bloodborne', 'release_year': '2015', 'rating': 'M', 'genre': 'Action-Adventure, Survival Horror'}
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {
        'games': games
    })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {'game': game})
