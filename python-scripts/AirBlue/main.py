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
    doc = lxml.html.fromstring(response.content)

    dummy_str = '//table[@id="trip_1_date_' + "{}_{}_{}".format(args['AM'][:4], args['AM'][5:], args['AD']) + '"]'
    flights_from = doc.xpath('{}/tbody/tr'.format(dummy_str))
    cabin_classes = doc.xpath('{}/thead/tr[2]/th/span/text()'.format(dummy_str))
    base1 = []
    for item in flights_from:
        base1.append({'Flight': item.xpath('td[1]/text()'),
                      'Depart': item.xpath('td[2]/text()'),
                      'Arrive': item.xpath('td[4]/text()'),
                      'Price': []})
        curs = item.xpath('td[@rowspan]/label/span/b/text()')
        costs = item.xpath('td[@rowspan]/label/span/text()')
        i = 0
        for currency in curs:
            base1[-1]['Price'].append({cabin_classes[i]: {currency: costs[i]}})
            i += 1

    if args['TT'] == 'OW':
        for item in base1:
            print(item)
    else:
        dummy_str = '//table[@id="trip_2_date_' + "{}_{}_{}".format(args['RM'][:4], args['RM'][5:], args['RD']) + '"]'
        flights_back = doc.xpath('{}/tbody/tr'.format(dummy_str))
        cabin_classes = doc.xpath('{}/thead/tr[2]/th/span/text()'.format(dummy_str))
        base2 = []
        for item in flights_back:
            base2.append({'Flight': item.xpath('td[1]/text()'),
                          'Depart': item.xpath('td[2]/text()'),
                          'Arrive': item.xpath('td[4]/text()'),
                          'Price': []})
            curs = item.xpath('td[@rowspan]/label/span/b/text()')
            costs = item.xpath('td[@rowspan]/label/span/text()')
            i = 0
            for currency in curs:
                base2[-1]['Price'].append({cabin_classes[i]: {currency: costs[i]}})
                i += 1
        print(base2)




if __name__ == "__main__":
    main(args_parse.create_arg_parser())
    # main(1)
