import sqlite3
import sys
import requests
import lxml.html
import itertools


def get_city_codes():
    """
    Get IATA city codes from AirBlue.com.
    :return: all possible routes.
    """
    try:
        response = requests.get('https://www.airblue.com/')
    except requests.ConnectionError as e:
        print(e)
        sys.exit()
    doc = lxml.html.fromstring(response.content)
    from_city = doc.xpath('.//select[@name="DC"]/option[position()>1]/@value')
    to_city = doc.xpath('.//select[@name="AC"]/option[position()>1]/@value')
    combinations = itertools.product(from_city, to_city)
    combinations = [item for item in combinations if item[0] != item[1]]
    return combinations


def sql_connection():
    """
    Create connection to database.
    :return: connect object.
    """
    try:
        con = sqlite3.connect('AirBlue_base.db')
        return con
    except sqlite3.Error as e:
        print(e)
        sys.exit()


def create_table(con):
    """
    Create table and fill her with routs.
    :param con: connection object.
    """
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS IATA('
                   'id INTEGER PRIMARY KEY NOT NULL,'
                   'from_city TEXT NOT NULL, to_city TEXT NOT NULL)')

    if not cursor.execute('SELECT * FROM IATA WHERE id=1').fetchone():
        cursor.executemany('INSERT INTO IATA(from_city, to_city) VALUES (?,?)', get_city_codes())
    con.commit()


def get_from_base(from_city, to_city):
    """
    Get combinations from our database.
    :return: all possible routes.
    """
    cursor = sql_connection().cursor()
    return cursor.execute('SELECT from_city, to_city FROM IATA WHERE from_city=\'{}\' AND to_city=\'{}\''.format(
        from_city, to_city
    )).fetchone()


if __name__ == '__main__':
    create_table(sql_connection())
