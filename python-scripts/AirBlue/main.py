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


def main():
    args = url_params(args_parse.create_arg_parser())
    Flights = collections.namedtuple('Flights', "Flight Depart Arrive Price")
    base_url = "https://www.airblue.com/bookings/flight_selection.aspx"
    response = requests.get(base_url, params=args)
    doc = lxml.html.fromstring(response.content)

    # Working with first flight.
    dummy_str = '//table[@id="trip_1_date_' + "{}_{}_{}".format(args['AM'][:4], args['AM'][5:], args['AD']) + '"]'
    flights_from = doc.xpath('{}/tbody/tr[1]'.format(dummy_str))
    print(flights_from)
    cabin_classes = doc.xpath('{}/thead/tr[2]/th/span/text()'.format(dummy_str))
    base1 = []
    for item in flights_from:
        base1.append(Flights(
            item.xpath('td[1]/text()')[0].rstrip(),
            item.xpath('td[2]/text()')[0],
            item.xpath('td[4]/text()')[0],
            []
        ))
        curs = item.xpath('td[@rowspan]/label/span/b/text()')
        costs = item.xpath('td[@rowspan]/label/span/text()')
        i = 0
        for currency in curs:
            base1[-1].Price.append({cabin_classes[i]: {currency: costs[i]}})
            i += 1

    if args['TT'] == 'OW':
        flights_print.one_way_print(base1)
    else:
        # Working with second flight.
        dummy_str = '//table[@id="trip_2_date_' + "{}_{}_{}".format(args['RM'][:4], args['RM'][5:], args['RD']) + '"]'
        flights_back = doc.xpath('{}/tbody/tr[1]'.format(dummy_str))
        cabin_classes = doc.xpath('{}/thead/tr[2]/th/span/text()'.format(dummy_str))
        base2 = []
        for item in flights_back:
            base2.append(Flights(
                item.xpath('td[1]/text()')[0].rstrip(),
                item.xpath('td[2]/text()')[0],
                item.xpath('td[4]/text()')[0],
                []
            ))
            curs = item.xpath('td[@rowspan]/label/span/b/text()')
            costs = item.xpath('td[@rowspan]/label/span/text()')
            i = 0
            for currency in curs:
                base2[-1].Price.append({cabin_classes[i]: {currency: costs[i]}})
                i += 1
        flights_print.round_trip_print(base1, base2)


if __name__ == "__main__":
    main()
