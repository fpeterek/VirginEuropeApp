import re
from datetime import datetime


class InvalidAirportException(Exception):
    pass


__airport_re = re.compile('([A-Z]{4}[)])$')
__classes = ['business', 'economy', 'first']


def parse_airport(query: str) -> str:
    if not __airport_re.search(query):
        print("Invalid airport", query)
        raise InvalidAirportException('Invalid airport')
    print("Valid airport:", query[-5:-1])
    return query[-5:-1]


def validate_date(date: str) -> bool:
    month, day, year = date.split('/')

    try:
        datetime(int(year), int(month), int(day))
    except ValueError:
        return False

    return True


def validate_class(cls: str) -> bool:
    return cls in __classes
