import requests

from VirginEurope.api.conf import Conf


def book_flights(fl1: int, fl2: int, pax: int, cls: str) -> str:
    params = {'fl1': fl1, 'pax': pax, 'cls': cls}

    if fl2 is not None:
        params['fl2'] = fl2

    resp = requests.get(f'{Conf.url}/book-flights', params=params)

    if resp.status_code != 200:
        return '{"error": "Server unavailable"}'

    return resp.text
