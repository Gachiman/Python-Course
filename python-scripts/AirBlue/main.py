import requests
import lxml.html
import collections
import sys
import datetime
from decimal import Decimal

import args_parse
import flights_print


Flight = collections.namedtuple("Flight", "flight date depart arrive duration fare_family currency price")


def url_params(args_):
    """
    Create one object for making get request with him.
    :param args_: flight arguments from args_parse.py.
    :return: one dict object, containing all parameters.
    """
    args = {
        "TT": "OW",
        "DC": args_.from_city,
        "AC": args_.to_city,
        "AM": args_.departure_date.strftime("%Y-%m"),
        "AD": args_.departure_date.strftime("%d"),
        "PA": "1"
    }

    if args_.return_date:
        args["TT"] = "RT"
        args["RM"] = args_.return_date.strftime("%Y-%m")
        args["RD"] = args_.return_date.strftime("%d")

    return args


def calculate_duration(arrive_time, depart_time):
    """
    Calculate flight duration.
    :param arrive_time: (str) - arrive time in format YYYY-MM-DD.
    :param depart_time: (str) - departure time in format YYYY-MM-DD.
    :return: (str) - duration.
    """
    arrive_time = datetime.datetime.strptime(arrive_time, "%I:%M %p")
    depart_time = datetime.datetime.strptime(depart_time, "%I:%M %p")
    duration = (arrive_time - depart_time).total_seconds()
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    return "{}h {}m".format(hours, minutes)


def fill_database(args, doc, way):
    """
    Takes data from airblue.com and saving them in database.
    :param doc: html document.
    :param way: dummy string to select flights.
    :param args: flight select arguments.
    :return: Database with fields: Flight, Depart, Arrive, Price (Fare_family, Currency, Cost).
    """
    flights_to = (doc.xpath('//div[@id="trip_{}"]/table/tbody/tr'.format(way)))
    if way == 1:
        from_to_info = "{}-{}".format(args["DC"], args["AC"])
        date = "{}-{}".format(args["AM"], args["AD"])
    else:
        from_to_info = "{}-{}".format(args["AC"], args["DC"])
        date = "{}-{}".format(args["RM"], args["RD"])

    flights = []
    for item in flights_to:
        curs = (item.xpath('./td[@rowspan]/label/span/b/text()'))
        fare_family = iter(doc.xpath('//div[@id="trip_{}"]/table/thead/tr[2]/th/span/text()'.format(way)))
        costs = iter(item.xpath('./td[@rowspan]/label/span/text()'))
        depart_time = item.xpath('./td[2]/text()')[0]
        arrive_time = item.xpath('./td[4]/text()')[0]
        duration = calculate_duration(arrive_time, depart_time)

        for currency in curs:
            flights.append(Flight(
                "{}:{}".format(from_to_info, item.xpath('./td[1]/text()')[0].rstrip()),  # flight
                date,
                depart_time,
                arrive_time,
                duration,
                next(fare_family),
                currency,
                Decimal(next(costs).replace(',', '.'))
            ))

    return flights


def main():
    args = url_params(args_parse.create_arg_parser())
    base_url = "https://www.airblue.com/bookings/flight_selection.aspx"

    try:
        response = requests.get(base_url, params=args)
    except requests.ConnectionError as e:
        print(e)
        sys.exit()
    doc = lxml.html.fromstring(response.content)

    # Working with first flight.
    flights_1 = fill_database(args, doc, "1")
    if args["TT"] == "OW":
        flights_print.one_way_print(flights_1)
    else:
        # Working with second flight.
        flights_2 = fill_database(args, doc, "2")
        flights_print.round_trip_print(flights_1, flights_2)


if __name__ == "__main__":
    main()
