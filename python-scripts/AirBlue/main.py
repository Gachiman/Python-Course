import requests
import lxml.html
import collections
import sys

import args_parse
import flights_print


Flight = collections.namedtuple("Flight", "flight depart arrive price")
Money_things = collections.namedtuple("Money_things", "fare_family currency cost")


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


def fill_database(doc, dummy_str):
    """
    Takes data from airblue.com and saving them in database.
    :param doc: html document.
    :param dummy_str: dummy string to select flights.
    :return: Database with fields: Flight, Depart, Arrive, Price (Fare_family, Currency, Cost).
    """
    flights_to = (doc.xpath('{}/tbody/tr'.format(dummy_str)))

    flights = []
    for item in flights_to:
        flights.append(Flight(
            item.xpath('./td[1]/text()')[0].rstrip(),  # flight
            item.xpath('./td[2]/text()')[0],  # depart
            item.xpath('./td[4]/text()')[0],  # arrive
            []  # price
        ))

        fare_family = iter(doc.xpath('{}/thead/tr[2]/th/span/text()'.format(dummy_str)))
        curs = (item.xpath('./td[@rowspan]/label/span/b/text()'))
        costs = iter(item.xpath('./td[@rowspan]/label/span/text()'))
        for currency in curs:
            flights[-1].price.append(Money_things(
                next(fare_family),
                currency,
                next(costs)
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
    dummy_str = '//table[@id="trip_1_date_{}_{}_{}"]'.format(args["AM"][:4], args["AM"][5:], args["AD"])
    flights_1 = fill_database(doc, dummy_str)

    if args["TT"] == "OW":
        flights_print.one_way_print(flights_1)
    else:
        # Working with second flight.
        dummy_str = '//table[@id="trip_2_date_{}_{}_{}"]'.format(args["RM"][:4], args["RM"][5:], args["RD"])
        flights_2 = fill_database(doc, dummy_str)

        flights_print.round_trip_print(flights_1, flights_2)


if __name__ == "__main__":
    main()
