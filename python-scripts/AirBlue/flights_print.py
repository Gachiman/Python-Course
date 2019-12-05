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
    duration = calculate_duration(info.Arrive, info.Depart)
    print("{}:\t Depart: {}\t Arrive: {}\t Duration: {}".format(info.Flight, info.Depart, info.Arrive,
                                                                duration))
    for cost in info.Price:
        print("Tariff: {}\tCurrency: {}\tCost: {}".format(list(cost.keys())[0],  # Need to do something with this
                                                          list(list(cost.values())[0].keys())[0],
                                                          list(list(cost.values())[0].values())[0]))
    print()


def one_way_print(base1):
    for flight in base1:
        display(flight)
        print()


def round_trip_print(base1, base2):
    combinations = tuple(itertools.product(base1, base2))
    costs = {}
    i = 0
    for item in combinations:
        cost1 = float(list(list(item[0].Price[-1].values())[0].values())[0].replace(',', '.'))
        cost2 = float(list(list(item[1].Price[-1].values())[0].values())[0].replace(',', '.'))
        costs[i] = cost1 + cost2
        i += 1
    costs = list(costs.items())
    costs.sort(key=lambda x: x[1])
    for item in costs:
        display(combinations[item[0]][0])
        display(combinations[item[0]][1])
        print("\nTOTAL COST: {}  {}\n\n\n".format(item[1],
                                                  list(list(combinations[item[0]][0].Price[-1].values())[0].keys())[0]))

