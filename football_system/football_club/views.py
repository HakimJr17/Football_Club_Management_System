from django.shortcuts import render
from .models import Players
from django.views.generic.detail import DetailView

# Create your views here.

def get_players(request):
    players = Players.objects.all()
    context = {
        'players' : players
    }
    return render(request, 'football_club/list_players.html', context)

    # I will use the DetailView because it is designed specifically for displaying a single object's 
    # details on a page. In our case, this could be the players, equipments, training sessions, 
    # incomes, matches, team, assignments models. 

