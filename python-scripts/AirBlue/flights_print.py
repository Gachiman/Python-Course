import itertools


def get_flight_string(info):
    """
    Forming information string about a particular flight.
    :param info: (namedtuple) - collection object with information about our flight.
    """
    return (
        '- {flight}'
        ' {departure_date} - {arrival_date} '
        '({duration}) '
        '{fare_family}'.format(**info._asdict())
    )


def print_flight(*flights):
    combinations = itertools.product(*flights)
    combinations = sorted(combinations, key=lambda item: sum(i.price for i in item))

    if not combinations:
        print('No flights found')

    for flight in combinations:
        print('\n'.join(get_flight_string(item) for item in flight))
        print(
            'TOTAL PRICE: {} {}\n'.format(
                sum(item.price for item in flight),
                flight[0].currency
            )
        )
