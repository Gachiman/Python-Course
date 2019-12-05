import datetime
import itertools


def calculate_duration(arrive_time, depart_time):
    """
    Calculate flight duration.
    :param arrive_time: (str) - arrive time in format DD.MM.YYYY.
    :param depart_time: (str) - departure time in format DD.MM.YYYY.
    :return: (str) - duration.
    """
    arrive_time = datetime.datetime.strptime(arrive_time, "%I:%M %p")
    depart_time = datetime.datetime.strptime(depart_time, "%I:%M %p")
    duration = (arrive_time - depart_time).total_seconds()
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    return "{}:{}".format(hours, minutes)


def display(info):
    """
    Displays information about a particular flight.
    :param info: (namedtuple) - collection object with information about our flight.
    """
    duration = calculate_duration(info.Arrive, info.Depart)
    print("{}:\t Depart: {}\t Arrive: {}\t Duration: {}".format(info.Flight, info.Depart, info.Arrive, duration))
    for cost in info.Price:
        print("Tariff: {}\tCurrency: {}\tCost: {}".format(cost.Cabin_class, cost.Currency, cost.Cost))
    print()


def one_way_print(base1):
    """
    If we are going one way.
    :param base1: list with our one-way flights.
    """
    for flight in base1:
        display(flight)
        print()


def round_trip_print(base1, base2):
    """
    If we are going round trip.
    :param base1: list with our first flights.
    :param base2: list with our second flights.
    """
    combinations = tuple(itertools.product(base1, base2))
    costs = {}
    i = 0
    for item in combinations:
        cost1 = float(item[0].Price[-1].Cost.replace(',', '.'))
        cost2 = float(item[1].Price[-1].Cost.replace(',', '.'))
        costs[i] = cost1 + cost2
        i += 1
    costs = list(costs.items())
    costs.sort(key=lambda x: x[1])
    for item in costs:
        display(combinations[item[0]][0])
        display(combinations[item[0]][1])
        print("\nTOTAL COST: {}  {}\n\n\n".format(item[1], combinations[item[0]][0].Price[-1].Currency))
