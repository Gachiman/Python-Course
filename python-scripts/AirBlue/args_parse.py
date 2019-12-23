import sys
import argparse
import re
import datetime
from dateutil.relativedelta import relativedelta

import database


def valid_city_code(code):
    """
    Check that the city IATA-code os correct.
    :param code: (str) - city IATA-code.
    :return: (str) - valid IATA-code.
    """
    if not re.search(r'\b[A-Z]{3}\b', code):
        raise argparse.ArgumentError(None, 'Invalid city IATA-code. There must be 3 uppercase characters.')
    return code


def valid_date(input_date):
    """
    Check data on correctly input.
    :param input_date: (str) - data in format YYYY-MM-DD or  DD-MM-YYYY.
    :return: (datetime) - valid datetime object.
    """
    if re.search(r'\b\d{2}-\d{2}-\d{4}', input_date):
        input_date = input_date[6:] + input_date[2:6] + input_date[:2]
    input_date = datetime.date.fromisoformat(input_date)
    if input_date < datetime.date.today():
        raise argparse.ArgumentError(None, 'Please select today or a future date for travel.')
    if input_date > datetime.date.today() + relativedelta(years=1):
        raise argparse.ArgumentError(None, 'Please, live in the present (date too in the future).')
    return input_date


def create_arg_parser():
    """
    Takes command line arguments using argparse.
    :return: argparse.Namespace - parsed arguments of valid type.
    """
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('from_city', type=valid_city_code, help='Origin city code: 3 capital letters (e.g. ISB)')
    arg_parser.add_argument('to_city', type=valid_city_code, help='Origin city code: 3 capital letters (e.g. ISB)')
    arg_parser.add_argument('departure_date', type=valid_date, help='Departure date: YYYY-MM-DD'
                                                                    ' or DD-MM-YYYY (without dropping zeros)')
    arg_parser.add_argument('return_date', nargs="?", type=valid_date, help='Departure date: YYYY-MM-DD'
                                                                            ' or DD-MM-YYYY(without dropping zeros)')

    try:
        our_args = arg_parser.parse_args()
        if our_args.return_date and (our_args.departure_date > our_args.return_date):
            raise argparse.ArgumentError(None, 'You can\'t return on an earlier date than you leave!')

        if our_args.from_city == our_args.to_city:
            raise argparse.ArgumentError(None, 'You already in this city!')

        if not database.get_from_base(our_args.from_city, our_args.to_city):
            raise argparse.ArgumentError(None, 'This route does not exists!')

    except argparse.ArgumentError as e:
        print(e)
        sys.exit()
    return our_args


if __name__ == '__main__':
    print(create_arg_parser())
