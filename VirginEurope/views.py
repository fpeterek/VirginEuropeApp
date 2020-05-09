import json

from django.http import HttpResponse
from django.shortcuts import render

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

    results = ['Kobeřice International', 'Singapore Changi', 'Frankfurt um Mainz', 'Munchen Airport',
                'Los Angeles International', 'Dubai International', 'Hamad International Airport',
                'Leoš Janáček Aiport', 'Václav Havel Airport']

    if request.is_ajax():
        results = json.dumps(list(filter(lambda x: request.GET.get('term', '') in x, results)))
    else:
        results = json.dumps(results)

    return HttpResponse(results, 'application/json')

