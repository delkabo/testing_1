import urllib.request
import xml.dom.minidom as minidom
import sqlite3
import datetime

def get_xml(url):
    try:
        web_file = urllib.request.urlopen(url)
        return web_file.read()
    except:
        pass

def get_valutes(xml_element):

    dom = minidom.parseString(xml_element)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'CharCode':
                    char_code = child.firstChild.data
        currency_dict[char_code] = value
    return currency_dict

def create_table(dbpath):
    table = 'testdb2'
    con = sqlite3.connect(dbpath)
    cur = con.cursor()

    query = F'CREATE TABLE IF NOT EXISTS {table} (id, name, surname)'
    cur.execute(query)
    con.commit()

    namet = 'lemon'
    surname = 'kisliy'

    query = F'INSERT INTO {table} VALUES (?,?,?)'

    l = 1
    while l < 3:
        data = (l, namet, surname)
        cur.execute(query, data)
        l = l + 1

    con.commit()

    con.close()


def read_table(path):
    table = 'testdb'

    con = sqlite3.connect(path)
    cur = con.cursor()

    query = F'SELECT * FROM {table}'
    cur.execute(query)

    date_fetched = cur.fetchall()

    currencies_list = []
    for line in date_fetched:
        currencies_list.append(list(line))

    con.close()

    print(currencies_list)


if __name__ == '__main__':
    url = 'https://cbr.ru/scripts/XML_daily.asp'
    db_path = "./test1.db"
    print(get_valutes(get_xml(url)))
    create_table(db_path)
    read_table(db_path)
    print()
