import json

from django.http import HttpResponse
from django.shortcuts import render

from VirginEurope import api
from VirginEurope.forms import BookFlightForm, OriginBox, DestinationBox


def index(request):
    if request.method == 'GET':
        orig = OriginBox()
        dest = DestinationBox()
        form = BookFlightForm()
        return render(request, 'page.html', {'orig': orig, 'dest': dest, 'form': form})
    else:
        orig = request.POST.get('origin')
        dest = request.POST.get('destination')
        date = request.POST.get('date')
        tcls = request.POST.get('cls')
        return HttpResponse(f'{{"origin":"{orig}", "destination":"{dest}", "date":"{date}", "class":"{tcls}"}}')


def tickets(request):
    return HttpResponse("My tickets")


def airport_autocomplete(request):

    if request.is_ajax():
        results = api.search_airports(request.GET.get('term', ''))
    else:
        results = api.search_airports('')

    return HttpResponse(results, 'application/json')

