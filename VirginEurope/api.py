import http.client
import requests

import urllib.parse

url = 'http://127.0.0.1:8080'


def search_airports(query: str) -> str:
    print(query)
    '''conn = http.client.HTTPConnection(url)
    params = urllib.parse.urlencode({'@q': query})
    conn.request('GET', '/airports', params)
    resp = conn.getresponse()'''

    params = {'q': query}
    resp = requests.get(f'{url}/airports', params=params)

    if resp.status_code != 200:
        resp.close()
        return ''

    res = resp.text
    print(res)
    return res
