"""
Views for locator app
"""

from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse

import geo_utils

from forms import AddTournamentForm, SearchForm
from models import Tournaments


def home(request):
    """
    Render home page
    """
    context = {}
    return render(request, 'home.html', context)


def add(request):
    """
    Handler for post/get for add tournaments page
    """
    if request.method == 'POST':
        form = AddTournamentForm(request.POST)
        if form.is_valid():
            record = form.save()
            return redirect('{}?id={}'.format(reverse('locator:results'), record.pk))
    else:
        form = AddTournamentForm()

    return render(request, 'add_tournament.html', {'form': form})


def results(request):
    """
    Get results page or 404
    """
    record_id = request.GET.get('id')
    tournament = get_object_or_404(Tournaments, pk=record_id)
    return render(request, 'results.html', {'tournament': tournament})


def search(request):
    """
    Handler for post/get for search tournaments page
    """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            return redirect('{}?state={}'.format(reverse('locator:search_results'), state))
    else:
        form = SearchForm

    return render(request, 'search.html', {'form': form})


def search_results(request):
    """
    Handler for search results page
    """
    state = request.GET.get('state')
    try:
        tournaments = Tournaments.objects.filter(
            state=state, start_date__gte=date.today()).order_by('start_date')
        latlons = []
        latlon_state = geo_utils.get_lat_lon(state)
        for tournament in tournaments:
            latlon = geo_utils.get_lat_lon(tournament.address)
            latlons.append((latlon[0], latlon[1], tournament.name))

    except Tournaments.DoesNotExist:
        tournaments = None
    return render(
        request, 'search_results.html',
        {'tournaments': tournaments, 'latlons': latlons,
        'latlon_state':latlon_state})


