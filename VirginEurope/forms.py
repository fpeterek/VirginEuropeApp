from django import forms

TRAVEL_CLASS = [
    ('economy', 'Economy'),
    ('business', 'Business'),
    ('first', 'First'),
]


class OriginBox(forms.Form):
    origin = forms.CharField(label='Origin', max_length=256, required=True,
                             widget=forms.TextInput(attrs={'id': 'origin_box', 'class': 'ui-widget'}))


class DestinationBox(forms.Form):
    destination = forms.CharField(label='Destination', max_length=256, required=True,
                                  widget=forms.TextInput(attrs={'id': 'destination_box', 'class': 'ui-widget'}))


class BookFlightForm(forms.Form):

    date = forms.DateField(
        label="Date",
        widget=forms.DateInput(attrs={'id': 'flight_date', 'class': 'datepicker', 'data-toggle': 'datepicker'}),
        required=True
    )
    cls = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=TRAVEL_CLASS,
    )
