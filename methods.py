import csv

import requests
from bs4 import BeautifulSoup
import os


# Функция читает файл с прокси-серверами и возвращает список серверов
def create_proxy_list(file_data):
    with open(file_data, 'r') as file:
        return file.read().split()


# Функция читает файл с бзер-агентами и возвращает список юзер-агентов
def create_useragent_list(file_data):
    with open(file_data, 'r') as file:
        return file.read().split('\n')


# Функция создаёт словарь прокси для последующего использования
# в requests в качестве параметра requests(url, proxies=proxy_for_request("адрес_прокси:порт"))
# Если прокси с аутофикацией то формат (логин:пароль@адрес_прокси:порт)
def proxy_for_request(proxy_string):
    return {
        "http": f"http://{proxy_string}",
        "https": f"http://{proxy_string}"
    }


# Проверка прокси на любом сайте + проверка сайта без прокси
def proxy_checker(url, list_proxy):
    url_checker_non_proxy(url)
    for item in list_proxy:
        req = ''
        try:
            req = requests.get(url, proxies=proxy_for_request(item), timeout=5)
            print(f"{url} - {req} - {item.split('@')[1]}")
        except requests.exceptions.RequestException:
            print(f"ERROR: {url} - {req} - {item.split('@')[1]}")


# Проверка сайта без прокси
def url_checker_non_proxy(url):
    try:
        req = requests.get(url, timeout=5)
        print(f"{url} - {req} - No proxy")
    except requests.exceptions.RequestException:
        print(f"ERROR: {url} - No proxy")


# Функция для запроса
def get_request(url, headers_dict, proxy_server_dict=None):
    return requests.get(url, headers=headers_dict, proxies=proxy_server_dict, timeout=20)


# Проверка User-Agent и IP-адрес
def ip_useragent_checker(headers_dict, proxy_server_dict=None):
    req = requests.get('https://tools.browsernative.com/', headers=headers_dict, proxies=proxy_server_dict, timeout=20)
    src = BeautifulSoup(req.text, 'lxml')
    return f"IP: {src.find('span', class_='mono red copydata').text}\n" \
           f"User-Agent: {src.find('span', class_='mono copydata').text}"


# Функция для аолучения списка файлов по имени папки
def creator_lisr_files(dir_name):
    return os.listdir(dir_name)


# Создается csv файл с шапкой таблицы
def creator_file_csv(file_name, *columns):
    try:
        with open(file_name, 'w', encoding='utf-8-sig', newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(
                (
                    columns
                )
            )
    except Exception:
        print('ERROR')
        return


# Добавление в таблицу, созданную в creator_file_csv, данных
def adder_data_in_file(file_name, *data):
    with open(file_name, 'a', encoding='utf-8-sig', newline="") as file:
        try:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(
                (
                    data
                )
            )
        except Exception:
            print('ERROR')
            return


def reader_file(file_name):
    # try:
        with open(file_name, 'r', encoding='utf-8-sig') as file:
            return file.read()

    # except Exception:
    #     print('ERROR')
    #     return ''
