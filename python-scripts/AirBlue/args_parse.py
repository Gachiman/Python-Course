import sys
import argparse
import datetime


DEP_CODES = ('AUH', 'DXB', 'ISB', 'JED', 'KHI', 'LHE', 'MED', 'MUX', 'PEW', 'UET', 'RUH', 'SHJ')
ARRIVE_CODES = ('AUH', 'DMM', 'DXB', 'ISB', 'JED', 'KHI', 'LHE', 'MED', 'MUX', 'MCT', 'PEW', 'RYK', 'RUH', 'SHJ', 'SKT')


def valid_departure_city(city_departure):
    """
    Check that the city IATA-code is in DEP_CODES.
    :param city_departure: (str) - city IATA-code.
    :return: (str) - valid city IATA-code.
    """
    if city_departure not in DEP_CODES:
        raise argparse.ArgumentError(None, "Invalid departure city IATA-code. Choose from list: {}".format(DEP_CODES))
    return city_departure


def valid_arrive_city(city_arrive):
    """
    Check that the city IATA-code is in DEP_CODES.
    :param city_arrive: (str) - city IATA-code.
    :return: (str) - valid city IATA-code.
    """
    if city_arrive not in ARRIVE_CODES:
        raise argparse.ArgumentError(None, "Invalid arrival city IATA-code. Choose from list: {}".format(ARRIVE_CODES))
    return city_arrive


def valid_date(date):
    """
    Check data on correctly input.
    :param date: (str) - data in format DD.MM.YYYY.
    :return: (datetime) - valid datetime object.
    """
    date = datetime.datetime.strptime(date, '%d.%m.%Y')
    if date < datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0):
        raise argparse.ArgumentError(None, "Please select today or a future date for travel.")
    return date


def create_arg_parser():
    """
    Takes command line arguments using argparse.
    :return: argparse.Namespace - parsed arguments of valid type.
    """
    def raise_value_error(err_msg):
        raise argparse.ArgumentError(None, err_msg)
    arg_parser = argparse.ArgumentParser()
    arg_parser.error = raise_value_error

    arg_parser.add_argument("from_city", type=valid_departure_city)
    arg_parser.add_argument("to_city", type=valid_arrive_city)
    arg_parser.add_argument("departure_date", type=valid_date)
    arg_parser.add_argument("return_date", nargs='?', type=valid_date)

    try:
        our_args = arg_parser.parse_args()
        if our_args.return_date and (our_args.departure_date > our_args.return_date):
            raise argparse.ArgumentError(None, "You can't return on an earlier date than you leave!")
        if our_args.from_city == our_args.to_city:
            raise argparse.ArgumentError(None, "You already in this city!")
    except argparse.ArgumentError as e:
        print(e)
        sys.exit()
    return our_args


if __name__ == "__main__":
    print(create_arg_parser())
