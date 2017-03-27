from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Score, Year


# Create your views here.
def home(request):
    players = Player.objects.all().prefetch_related('score_set')
    years = Year.objects.all().values_list('year', flat=True)  # List of year name
    rows = []
    for year in years:
        row = {year: []}
        for idx, player in enumerate(players):
            score = player.score_set.filter(year__year=year).values_list('score', flat=True)
            row[year].append({player: ' ,'.join(score)})
        rows.append(row)  # Add new row in our rows list
    context = {'players': players,
               'rows': rows}
    return render(request, 'player.html', context)
