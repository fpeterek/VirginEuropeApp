import requests

url = 'http://127.0.0.1:8080'


def search_airports(query: str) -> str:
    params = {'q': query}
    resp = requests.get(f'{url}/airports', params=params)

    if resp.status_code != 200:
        resp.close()
        return ''

    return resp.text
