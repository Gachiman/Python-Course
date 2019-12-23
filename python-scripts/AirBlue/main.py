import requests
import lxml.html
import collections
import sys
import datetime
from decimal import Decimal

import args_parse
import flights_print
import database


Flight = collections.namedtuple('Flight', 'flight departure_date arrival_date duration fare_family currency price')


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
        'AM': args_.departure_date.strftime('%Y-%m'),
        'AD': args_.departure_date.strftime('%d'),
        'PA': '1'
    }

    if args_.return_date:
        args['TT'] = 'RT'
        args['RM'] = args_.return_date.strftime('%Y-%m')
        args['RD'] = args_.return_date.strftime('%d')

    return args


def calculate_duration(arrive_time, depart_time):
    """
    Calculate flight duration.
    :param arrive_time: (str) - arrive time in format YYYY-MM-DD.
    :param depart_time: (str) - departure time in format YYYY-MM-DD.
    :return: (str) - duration.
    """
    duration = (arrive_time - depart_time).total_seconds()
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    return '{}h {}m'.format(hours, minutes)


def parse_flights(args, doc, way):
    """
    Takes data from airblue.com and saving them in database.
    :param doc: html document.
    :param way: dummy string to select flights.
    :param args: flight select arguments.
    :return: Database with fields: flight departure_date arrival_date duration fare_family currency price.
    """
    flights_to = (doc.xpath('.//div[@id="trip_{}"]/table[contains(@class, "requested-date")]/tbody/tr'.format(way)))
    if way == '1':
        from_to_info = '{}-{}'.format(args['DC'], args['AC'])
        date = '{}-{}'.format(args['AM'], args['AD'])
    else:
        from_to_info = '{}-{}'.format(args['AC'], args['DC'])
        date = '{}-{}'.format(args['RM'], args['RD'])

    flights = []
    for item in flights_to:

        if (item.xpath('./@class'))[0] == 'no_flights_found':
            continue

        curs = (item.xpath('./td[@rowspan]/label/span/b/text()'))
        fare_family = iter(doc.xpath('.//div[@id="trip_{}"]/table[contains(@class, "requested-date")]'
                                     '/thead/tr[2]/th/span/text()'.format(way)))
        costs = iter(item.xpath('./td[@rowspan]/label/span/text()'))

        depart_time = item.xpath('./td[2]/text()')[0]
        arrive_time = item.xpath('./td[4]/text()')[0]
        departure_date = datetime.datetime.strptime(date + depart_time, '%Y-%m-%d%I:%M %p')
        arrival_date = datetime.datetime.strptime(date + arrive_time, '%Y-%m-%d%I:%M %p')

        if arrival_date < departure_date:
            arrival_date += datetime.timedelta(days=1)
        duration = calculate_duration(arrival_date, departure_date)

        for currency in curs:
            flights.append(Flight(
                '{}:{}'.format(from_to_info, item.xpath('./td[1]/text()')[0].rstrip()),  # flight
                departure_date.strftime('%Y-%m-%d %I:%M %p'),
                arrival_date.strftime('%Y-%m-%d %I:%M %p'),
                duration,
                next(fare_family),
                currency,
                Decimal(next(costs).replace(',', '.'))
            ))

    return flights


def main():
    args = url_params(args_parse.create_arg_parser())
    base_url = 'https://www.airblue.com/bookings/flight_selection.aspx'

    try:
        response = requests.get(base_url, params=args)
    except requests.ConnectionError as e:
        print(e)
        sys.exit()
    doc = lxml.html.fromstring(response.content)

    # Working with outbound flight.
    out_flights = parse_flights(args, doc, '1')
    if args['TT'] == 'OW':
        flights_print.print_flight(out_flights)
    else:
        # Working with inbound flight.
        inb_flights = parse_flights(args, doc, '2')
        flights_print.print_flight(out_flights, inb_flights)


if __name__ == '__main__':
    database.create_table(database.sql_connection())
    main()
