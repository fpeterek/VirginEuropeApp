import requests

from VirginEurope.api.conf import Conf


def search_airports(query: str) -> str:
    params = {'q': query}
    resp = requests.get(f'{Conf.url}/airports', params=params)

    if resp.status_code != 200:
        resp.close()
        return ''

    return resp.text
