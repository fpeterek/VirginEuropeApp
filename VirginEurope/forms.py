from django import forms

TRAVEL_CLASS = [
    ('economy', 'Economy'),
    ('business', 'Business'),
    ('first', 'First'),
]


class OriginBox(forms.Form):
    origin = forms.CharField(max_length=256, required=True, label='', widget=forms.TextInput(
        attrs={'id': 'origin_box',
               'class': 'airport-select ui-widget',
               'placeholder': 'Origin'}))


class DestinationBox(forms.Form):
    destination = forms.CharField(max_length=256, required=True, label='', widget=forms.TextInput(
        attrs={'id': 'destination_box',
               'class': 'airport-select ui-widget',
               'placeholder': 'Destination'}))


class BookFlightForm(forms.Form):

    date = forms.DateField(
        label='',
        widget=forms.DateInput(attrs={'id': 'flight_date', 'class': 'datepicker', 'data-toggle': 'datepicker',
                                      'placeholder': 'Departure'}),
        required=True
    )
    cls = forms.ChoiceField(
        label='',
        required=True,
        widget=forms.Select(attrs={'class': 'class-select'}),
        choices=TRAVEL_CLASS,
    )
