import itertools


def display(info):
    """
    Displays information about a particular flight.
    :param info: (namedtuple) - collection object with information about our flight.
    """
    print("- {} {} {} - {} {} ({}) {} {} {}".format(info.flight, info.date, info.depart, info.date, info.arrive,
                                                    info.duration, info.fare_family, info.price, info.currency))
    print()


def one_way_print(flights_1):
    """
    If we are going one way.
    :param flights_1: list with our one-way flights.
    """
    for flight in flights_1:
        display(flight)
        print()


def round_trip_print(flights_1, flights_2):
    """
    If we are going round trip.
    :param flights_1: list with our first flights.
    :param flights_2: list with our second flights.
    """
    combinations = tuple(itertools.product(flights_1, flights_2))
    combinations = sorted(combinations, key=lambda x: x[0].price + x[1].price)
    for item in combinations:
        display(item[0])
        display(item[1])
        print("TOTAL COST: {}  {}\n\n\n".format(item[0].price + item[1].price, item[0].currency))
