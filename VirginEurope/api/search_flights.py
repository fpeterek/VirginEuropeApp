import json

import requests

from VirginEurope.api.conf import Conf


def _flight_to_url_params(first: int = None, second: int = None, cls: str = None) -> str:
    params = []
    if first:
        params.append(f"fl1='{first}'")
    if second:
        params.append(f"fl2='{second}'")
    if cls:
        params.append(f"cls='{cls}'")

    return str.join('&', params)


class SingleSegment:
    def __init__(self, flight: str, flight_id: int, date: str, price: int, cls: str):
        self.flight = flight
        self.id = flight_id
        self.date = date
        self.price = price
        self.cls = cls

    @staticmethod
    def parse_from(d: dict, cls: str):
        return SingleSegment(d['flight'], d['id'], d['date'], d['price'], cls)

    def __str__(self):
        return f'Flight {self.flight} on {self.date}, travel class {self.cls}, price {self.price}'

    @property
    def to_url_params(self) -> str:
        return _flight_to_url_params(first=self.id, cls=self.cls)


class TwoSegment:
    def __init__(self, flight1, id1, date1, flight2, id2, date2, price, cls):
        self.first_flight = flight1
        self.first_id = id1
        self.first_date = date1
        self.second_flight = flight2
        self.second_id = id2
        self.second_date = date2
        self.price = price
        self.cls = cls

    @staticmethod
    def parse_from(d: dict, cls: str):
        return TwoSegment(d['first'], d['first_id'], d['first_date'],
                          d['second'], d['second_id'], d['second_date'], d['price'], cls)

    def __str__(self):
        return f'First flight: {self.first_flight} on {self.first_date}, ' \
               f'Second flight: {self.second_flight} on {self.second_date}, ' \
               f'travel class {self.cls}, price {self.price}'

    @property
    def to_url_params(self) -> str:
        return _flight_to_url_params(first=self.first_id, second=self.second_id, cls=self.cls)


def parse_flights(resp: str, cls: str) -> list:
    data = json.loads(resp)
    if data.get('single_segment'):
        return list(map(lambda x: SingleSegment.parse_from(x, cls), data.get('flights', [])))
    if data.get('two_segment'):
        return list(map(lambda x: TwoSegment.parse_from(x, cls), data.get('flights', [])))

    return []


def search_flights(orig: str, dest: str, date: str, cls: str) -> list:
    data = {'orig': orig, 'dest': dest, 'date': date, 'cls': cls}
    resp = requests.post(f'{Conf.url}/find-flights', json=data)

    if resp.status_code != 200:
        return []

    return parse_flights(resp.text, cls)
