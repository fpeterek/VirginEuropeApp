import json

from django.http import HttpResponse
from django.shortcuts import render

from VirginEurope import api, util
from VirginEurope.forms import BookFlightForm, OriginBox, DestinationBox


def index(request):
    if request.method == 'GET':
        orig = OriginBox()
        dest = DestinationBox()
        form = BookFlightForm()
        return render(request, 'page.html', {'orig': orig, 'dest': dest, 'form': form})
    else:
        form = BookFlightForm(request.POST)
        orig_form = OriginBox(request.POST)
        dest_form = DestinationBox(request.POST)
        orig = ""
        dest = ""

        try:
            orig = util.parse_airport(request.POST.get('origin'))
        except util.InvalidAirportException as e:
            orig_form.add_error('origin', e)
        try:
            dest = util.parse_airport(request.POST.get('destination'))
        except util.InvalidAirportException as e:
            dest_form.add_error('destination', e)

        date = request.POST.get('date')
        tcls = request.POST.get('cls')

        if form.errors or orig_form.errors or dest_form.errors:
            return render(request, 'page.html', {'orig': orig_form, 'dest': dest_form, 'form': form})

        return HttpResponse(f'{{"origin":"{orig}", "destination":"{dest}", "date":"{date}", "class":"{tcls}"}}')


def tickets(request):
    return HttpResponse("My tickets")


def airport_autocomplete(request):

    if request.is_ajax():
        results = api.search_airports(request.GET.get('term', ''))
    else:
        results = api.search_airports('')

    return HttpResponse(results, 'application/json')

