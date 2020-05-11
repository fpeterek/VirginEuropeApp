import json

from django.http import HttpResponse
from django.shortcuts import render

from VirginEurope.api.book_flights import book_flights
from VirginEurope.api.list_tickets import list_tickets
from VirginEurope.api.search_airports import search_airports
from VirginEurope.api.search_flights import search_flights


from VirginEurope import util
from VirginEurope.forms import BookFlightForm, OriginBox, DestinationBox


def book(request):
    fl1 = request.GET.get('fl1', '').strip("'")
    fl2 = request.GET.get('fl2', '').strip("'")
    cls = request.GET.get('cls', '').strip("'")
    pax = request.GET.get('pax', '').strip("'")

    if not util.validate_class(cls):
        return render(request, 'message.html', {'message': 'Invalid class'})

    if not fl1 or not fl1.isdigit() or (fl2 and not fl2.isdigit()):
        return render(request, 'message.html', {'message': 'Invalid flight number'})

    if not pax or not pax.isdigit():
        return render(request, 'message.html', {'message': 'Invalid passenger'})

    resp = book_flights(fl1, fl2, pax, cls)
    print(resp)
    resp = json.loads(resp)

    if resp.get('success'):
        return render(request, 'message.html', {'message': 'Flight successfully booked. Thank you.'})

    return render(request, 'message.html', {'message': 'An unexpected error has occured. Please try again later.'})


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

        return render(request, 'list_flights.html', {'flights': search_flights(orig, dest, date, tcls)})


_true = ['true', '1']


def tickets(request):
    pax = request.GET.get('pax', '').strip("'")
    old = request.GET.get('old', 'false').strip("'").lower()

    if not pax.isdigit():
        return render(request, 'message.html', {'message': 'Invalid passenger'})

    try:
        flight_tickets = list_tickets(pax, old in _true)
    except Exception as e:
        return render(request, 'message.html', {'message': 'Unexpected error'})

    return render(request, 'list_tickets.html', {'tickets': flight_tickets})


def airport_autocomplete(request):

    if request.is_ajax():
        results = search_airports(request.GET.get('term', ''))
    else:
        results = search_airports('')

    return HttpResponse(results, 'application/json')
