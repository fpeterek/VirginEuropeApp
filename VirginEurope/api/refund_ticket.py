import json

import requests

from VirginEurope.api.conf import Conf


def refund(ticket: int) -> dict:
    params = {'id': ticket}

    resp = requests.delete(f'{Conf.url}/delete-ticket', params=params)

    if resp.status_code != 200:
        raise Exception('Call unsuccessful')

    return json.loads(resp.text)
