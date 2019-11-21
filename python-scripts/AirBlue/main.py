import requests
import lxml.html
import args_parse


def main(args):
    base_url = "https://www.airblue.com/bookings/flight_selection.aspx"
    if args.return_date:
        args = {'TT': 'RT', 'DC': args.from_city, 'AC': args.to_city, 'AM': args.departure_date.strftime("%Y-%m"),
                'AD': args.departure_date.strftime("%d"), 'RM': args.return_date.strftime("%Y-%m"),
                'RD': args.return_date.strftime("%d"), 'PA': '1'}
    else:
        args = {'TT': 'OW', 'DC': args.from_city, 'AC': args.to_city, 'AM': args.departure_date.strftime("%Y-%m"),
                'AD': args.departure_date.strftime("%d"), 'PA': '1'}
    response = requests.get(base_url, params=args)
    print(response)

    """base_url = "https://www.airblue.com/bookings/flight_selection.aspx?TT=OW&DC=KHI&AC=ISB&AM=2019-11&AD=22&PA=1"
    response = requests.get(base_url)
    doc = lxml.html.fromstring(response.content)
    first_ways = doc.xpath('//table[@class="flight_selection requested-date current-date column-count-1"]/tbody')
    print(first_ways)
    print(doc)"""


if __name__ == "__main__":
    main(args_parse.create_arg_parser())
    # main(1)
