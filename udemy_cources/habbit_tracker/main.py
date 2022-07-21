import requests
from datetime import datetime
from data import *

graphs_endpoint = f"{ENDPOINT}/{USERNAME}/graphs/{GRAPH}"
headers = {
    "X-USER-TOKEN": TOKEN,
}


def create_pixel(_date):
    pixel_data = {
        "date": date,
        "quantity": input("How many hours did you code?: "),
    }
    create = requests.post(url=GRAPHS_ENDPOINT, json=pixel_data, headers=headers)
    print(create.text)


def update_pixel(_date):
    pixel_endpoint = f"{graphs_endpoint}/{_date}"
    update_data = {
        "quantity": input("How many hours did you code?: "),
    }
    update = requests.put(url=pixel_endpoint, json=update_data, headers=headers)
    print(update.text)


def delete_pixel(_date):
    pixel_endpoint = f"{graphs_endpoint}/{_date}"
    delete = requests.delete(url=pixel_endpoint, headers=headers)
    print(delete.text)


def set_date():
    custom_date = input("Please input date in format DD.MM.YYYY: ")
    custom_date = datetime.strptime(custom_date, "%d.%m.%Y")
    custom_date = custom_date.strftime("%Y%m%d")
    return custom_date


task = int(input("Choose task:\n"
                 "1: Create pixel for today\n"
                 "2: Create pixel for custom date\n"
                 "3: Update pixel\n"
                 "4: Delete pixel\n"))

date = datetime.now()
date = date.strftime("%Y%m%d")
if task != 1:
    date = set_date()
    print(date)
if task == 1:
    create_pixel(date)
elif task == 2:
    create_pixel(date)
elif task == 3:
    update_pixel(date)
elif task == 4:
    delete_pixel(date)
