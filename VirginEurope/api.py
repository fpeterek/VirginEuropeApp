import requests

url = 'http://127.0.0.1:8080'


def search_airports(query: str) -> str:
    params = {'q': query}
    resp = requests.get(f'{url}/airports', params=params)

    if resp.status_code != 200:
        resp.close()
        return ''

    return resp.text


def search_flights(orig: str, dest: str, date: str, cls: str) -> str:

    data = {'orig': orig, 'dest': dest, 'date': date, 'cls': cls}
    resp = requests.post(f'{url}/find-flights', json=data)

    if resp.status_code != 200:
        return '{}'

    return resp.text
