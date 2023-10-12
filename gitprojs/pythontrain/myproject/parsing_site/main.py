import csv
import os
import unicodedata
from datetime import datetime
import time
import requests
import json
from bs4 import BeautifulSoup


def read_page():
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64)"
                             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    if not os.path.exists('date'):
        os.mkdir('date')

    r = requests.get('https://www.avito.ru/moskva/avtomobili', headers=headers)

    with open('date/page.html', 'w') as file:
        file.write(r.text)

    with open('date/page.html', 'r') as file:
        page_html = file.read()

    soup = BeautifulSoup(page_html, 'lxml')
    soup.find_all('div', class_='ya-unit-title')

    pages_count = int(soup.find('div', class_='pagination-pages').find_all("a")[-2].text)
    print(pages_count)

    for i in range(1, 2):
        url = f'https://www.avito.ru/moskva/avtomobili?p={i}&radius=0'
        r = requests.get(url, headers=headers).text

        with open(f'date/page_{i}.html', 'w') as file:
            file.write(r)

    return pages_count


def write_in(page_count):

    cur_date = datetime.now().strftime("%d_%m_%Y")

    with open(f'scv_file_{cur_date}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow((
            "Наименование",
            "Цена"
        ))

    cars_base = []
    for i in range(1, 2):

        with open(f'date/page_{i}.html', 'r') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        item_cars = soup.find_all('div', class_='iva-item-content-rejJg')

        for item in item_cars:
            car_name = item.find('h3', class_='title-root-zZCwT').text.strip()
            car_price = item.find('span', class_='price-text-_YGDY').text.strip(" ₽")

            car_price = unicodedata.normalize("NFKD", car_price)

            print(f'Наименование: {car_name}, Цена: {car_price}')

            cars_base.append({
                'car_name': car_name,
                'price_car': car_price
            })

            with open(f'csv_file_{cur_date}.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow((
                    car_name,
                    car_price
                ))

        time.sleep(2)

    with open(f"json_file_{cur_date}.json", "w") as file:
        json.dump(cars_base, file, indent=4, ensure_ascii=False)




def main():
    page_count = read_page()
    write_in(page_count)


if __name__ == '__main__':
    main()
