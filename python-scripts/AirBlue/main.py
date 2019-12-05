import requests
import lxml.html
import collections
import args_parse
import flights_print


def url_params(args_):
    """
    Create one object for making get request with him.
    :param args_: flight arguments from args_parse.py.
    :return: one dict object, containing all parameters.
    """
    args = {
        'TT': 'OW',
        'DC': args_.from_city,
        'AC': args_.to_city,
        'AM': args_.departure_date.strftime("%Y-%m"),
        'AD': args_.departure_date.strftime("%d"),
        'PA': '1'
    }

    if args_.return_date:
        args["TT"] = "RT"
        args["RM"] = args_.return_date.strftime("%Y-%m")
        args["RD"] = args_.return_date.strftime("%d")

    return args


def fill_database(flights_to, cabin_classes):
    """
    Takes data from airblue.com and saving them in database.
    :param flights_to: Flights base.
    :param cabin_classes: Economy / Standard (1 Bag).
    :return: Database with fields: Flight, Depart, Arrive, Price (Cabin_class, Currency, Cost).
    """
    flights = collections.namedtuple('Flights', "Flight Depart Arrive Price")
    money_things = collections.namedtuple("money_things", "Cabin_class Currency Cost")

    base = []
    for item in flights_to:
        base.append(flights(
            item.xpath('td[1]/text()')[0].rstrip(),  # Flight
            item.xpath('td[2]/text()')[0],  # Depart
            item.xpath('td[4]/text()')[0],  # Arrive
            []  # Price
        ))

        curs = (item.xpath('td[@rowspan]/label/span/b/text()'))
        costs = iter(item.xpath('td[@rowspan]/label/span/text()'))
        for currency in curs:
            base[-1].Price.append(money_things(
                next(cabin_classes),
                currency,
                next(costs)
            ))

    return base


def main():
    args = url_params(args_parse.create_arg_parser())
    base_url = "https://www.airblue.com/bookings/flight_selection.aspx"
    response = requests.get(base_url, params=args)
    doc = lxml.html.fromstring(response.content)

    # Working with first flight.
    dummy_str = '//table[@id="trip_1_date_' + "{}_{}_{}".format(args['AM'][:4], args['AM'][5:], args['AD']) + '"]'
    flights_from = (doc.xpath('{}/tbody/tr[1]'.format(dummy_str)))
    cabin_classes = iter(doc.xpath('{}/thead/tr[2]/th/span/text()'.format(dummy_str)))
    base1 = fill_database(flights_from, cabin_classes)

    if args['TT'] == 'OW':
        flights_print.one_way_print(base1)
    else:
        # Working with second flight.
        dummy_str = '//table[@id="trip_2_date_' + "{}_{}_{}".format(args['RM'][:4], args['RM'][5:], args['RD']) + '"]'
        flights_back = (doc.xpath('{}/tbody/tr[1]'.format(dummy_str)))
        cabin_classes = iter(doc.xpath('{}/thead/tr[2]/th/span/text()'.format(dummy_str)))
        base2 = fill_database(flights_back, cabin_classes)

        flights_print.round_trip_print(base1, base2)


if __name__ == "__main__":
    main()
