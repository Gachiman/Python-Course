import sys
import argparse
import datetime


def valid_departure_city(city_departure):
    try:
        if city_departure not in ('AUH', 'DXB', 'ISB', 'JED', 'KHI', 'LHE', 'MED', 'MUX', 'PEW', 'UET', 'RUH', 'SHJ'):
            raise RuntimeError
    except RuntimeError:
        city_departure = valid_departure_city(input("Input correct city code: "))
    return city_departure


def valid_arrive_city(city_arrive):
    try:
        if city_arrive not in ('AUH', 'DMM', 'DXB', 'ISB', 'JED', 'KHI', 'LHE', 'MED', 'MUX', 'MCT',
                               'PEW', 'RYK', 'RUH', 'SHJ', 'SKT'):
            raise RuntimeError
    except RuntimeError:
        city_arrive = valid_arrive_city(input("Input correct city code: "))
    return city_arrive


def valid_date(date_):
    date_ = datetime.datetime.strptime(date_, '%d.%m.%Y')
    try:
        if date_ < datetime.datetime.today():
            raise RuntimeError
    except RuntimeError:
        date_ = valid_date(input("Please select today or a future date for travel: "))
    return date_


def create_arg_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("from_city", type=valid_departure_city)
    arg_parser.add_argument("to_city", type=valid_arrive_city)
    arg_parser.add_argument("departure_date", type=valid_date)
    arg_parser.add_argument("return_date", nargs='?', type=valid_date)
    our_args = arg_parser.parse_args()
    try:
        if our_args.return_date and (our_args.departure_date > our_args.return_date):
            raise RuntimeError()
    except RuntimeError:
        sys.exit("You can't return on an earlier date than you leave")  # How I can repeat command line params input?
    return our_args


if __name__ == "__main__":
    print(create_arg_parser())
