import os
import time
import asyncio
import aiohttp

from methods import *
import requests
from bs4 import BeautifulSoup

list_proxy = create_proxy_list('datapool/proxy.txt')
proxy_one = proxy_for_request(list_proxy[0])
user_agents_list = create_useragent_list('datapool/user_agents_decktop.txt')
headers = {"user-agent": f"{user_agents_list[200]}"}
url_check_https = 'https://2ip.ru/'
url_check_http = 'http://checkip.dyndns.org'
url = 'https://vbankcenter.ru/contragent/1145256007577'
url_proxy = 'https://proxy6.net'
url_mail = 'https://mail.ru/'
url_kinosal = 'https://forum.kinozal.me/index.php'
url_check_useragent = 'https://ciox.ru/check-user-agent'
url_check_ip_and_useragent = 'https://tools.browsernative.com/'

# print(proxy_one['https'].split('@')[1].split(':')[0])
# print(headers)
# proxy_checker(url, list_proxy)
# print(get_request(url_check_ip_and_useragent, headers, proxy_one).cookies)
# print(ip_useragent_checker(headers, proxy_one))

if not os.path.exists(f"1111"):
    os.mkdir(f"1111")

url = 'https://vbankcenter.ru/contragent/codes/68321?size=150'


req = requests.get(url, proxies=None, headers=None).text
src = BeautifulSoup(req, 'lxml')
list_org = src.findAll('h5', class_='flex items-center pb-2 lg:pb-3.5 text-xl')
list_urls = []

for item in list_org:
    list_urls.append(f"https://vbankcenter.ru{item.find('a', class_='overlap text-blue').get('href')}")
print(list_urls)
start = time.time()
session = requests.Session()
count = 1
for item in list_urls:
    print(f"{count} - {session.get(item)}")
    count += 1
print(time.time() - start)

