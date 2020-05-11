import datetime
import json

import requests

from VirginEurope.api.conf import Conf


class Ticket:
    def __init__(self, d: dict):
        self.id = d['id']
        self.flight = d['flight']
        self.departure = datetime.datetime.strptime(f'{d["date"]} {d["departure"]}', '%Y-%m-%d %H:%M:%S')
        self.cls = d['class']
        self.meal = d['meal']
        self.allowance = d['allowance']
        self.seat = d['seat']
        self.destination = d['destination']
        self.origin = d['origin']
        self.equipment = d['equipment']

    @property
    def pretty_departure(self):
        return self.departure.strftime('%d.%m.%Y %H:%M')

    @property
    def pretty_class(self):
        return self.cls.capitalize()

    @property
    def pretty_flight(self):
        return f'VU{int(self.flight[2:])}'

    @property
    def pretty_meal(self):
        return self.meal.capitalize()

    @property
    def is_old(self):
        return datetime.datetime.now() > self.departure


def list_tickets(pax: int, old: bool = False) -> list:
    params = {'pax': pax, 'all': old}

    resp = requests.get(f'{Conf.url}/list-tickets', params=params)

    if resp.status_code != 200:
        raise Exception('Call unsuccessful')

    obj = json.loads(resp.text)

    if obj.get('error'):
        raise Exception(str(obj.get('error')))

    tickets = obj.get('tickets')
    if tickets is not None:
        return list(reversed(sorted(map(lambda x: Ticket(x), tickets), key=lambda ticket: ticket.departure)))

    return []
