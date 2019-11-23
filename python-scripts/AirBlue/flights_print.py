import datetime
import itertools


def display(info):
    duration = (datetime.datetime.strptime(info.Arrive, "%I:%M %p")
                - datetime.datetime.strptime(info.Depart, "%I:%M %p")).total_seconds()
    duration = "{}:{}".format(int(duration // 3600), int((duration % 3600) // 60))

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

