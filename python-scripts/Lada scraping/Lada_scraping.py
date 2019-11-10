import requests
import lxml.html
import json


def transform(cars):
    res = []
    for car in cars:
        res.append({
            'model': car,
            'cheap': {
                'title': cars[car][2],
                'price': cars[car][3]
            },
            'expensive': {
                'title': cars[car][0],
                'price': cars[car][1]
            },
            'price_list': cars[car][4]
        })
    return res


def parser():
    car_base = {}
    url = 'http://www.lada.ru'
    response = requests.get(url)
    doc = lxml.html.fromstring(response.content)
    model_row = '/html/body/section[1]/div[1]/div[1]/div/a[1]'
    models = iter(doc.xpath('{}/h5/text()'.format(model_row)))
    links = (url + link for link in doc.xpath('{}/@href'.format(model_row)))
    cars = (lxml.html.fromstring(requests.get(link).content) for link in links)

    prices = '//div[@itemprop="offers"]'
    for item in cars:
        car_base[next(models)] = (*item.xpath('{}[last()]/div[1]/p/text()'.format(prices)),
                                  *item.xpath('{}[last()]/@price'.format(prices)),
                                  *item.xpath('{}[1]/div[1]/p/text()'.format(prices)),
                                  *item.xpath('{}[1]/@price'.format(prices)),
                                  url + str(*item.xpath('//*[@id="all_compl"]/@href')))

    with open('cars.json', 'w', encoding='utf-8') as output_file:
        json.dump(transform(car_base), output_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    parser()
