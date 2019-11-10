import requests
import lxml.html
import json
import collections


def parser():
    car_base = []
    car = collections.namedtuple('car', "car_name highest hi_price lowest lo_price pdf")
    url = 'http://www.lada.ru'
    html = requests.get(url)
    doc = lxml.html.fromstring(html.content)
    models = doc.xpath('/html/body/section[1]/div[1]/div[1]/div/a[1]/h5/text()')
    links = doc.xpath('/html/body/section[1]/div[1]/div[1]/div/a[1]/@href')
    links = [url + link for link in links]
    cars = [lxml.html.fromstring(requests.get(link).content) for link in links]

    i = 0
    for item in cars:
        car_base.append(car(models[i], *item.xpath('//div[@itemprop="offers"][last()]/div[1]/p/text()'),
                            *item.xpath('//div[@itemprop="offers"][last()]/@price'),
                            *item.xpath('//div[@itemprop="offers"][1]/div[1]/p/text()'),
                            *item.xpath('//div[@itemprop="offers"][1]/@price'),
                            url + str(*item.xpath('//*[@id="all_compl"]/@href'))))
        i += 1

    with open('cars.json', 'w') as output_file:
        pass


if __name__ == "__main__":
    parser()
