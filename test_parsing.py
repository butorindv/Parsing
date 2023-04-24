import os
from requests.utils import DEFAULT_CA_BUNDLE_PATH

from methods import *
import requests
from bs4 import BeautifulSoup
from requests import Request, Session

list_proxy = create_proxy_list('datapool/proxy.txt')
proxy_1 = proxy_for_request(list_proxy[0])
proxy_2 = proxy_for_request(list_proxy[1])
user_agents_list = create_useragent_list('datapool/user_agents_decktop.txt')
header_1 = {"user-agent": f"{user_agents_list[200]}"}
header_2 = {"user-agent": f"{user_agents_list[1]}"}
url_check_https = 'https://2ip.ru/'
url_check_http = 'http://checkip.dyndns.org'
# url = 'https://vbankcenter.ru/contragent/1145256007577'
url_proxy = 'https://proxy6.net'
url_mail = 'https://mail.ru/'
url_kinosal = 'https://forum.kinozal.me/index.php'
url_check_useragent = 'https://ciox.ru/check-user-agent'
url_check_ip_and_useragent = 'https://tools.browsernative.com/'

# print(requests.options('https://api.github.com/repos/psf/requests/issues/482').content)

url = f'https://s3.landingfolio.com/inspiration?page=0'
response = requests.get(url=url, headers=header_2)
data = response.json()
# print(data)
for item in data:
    scr = item.get('screenshots')
    for id in scr:
        pass
        # print(f"https://landingfoliocom.imgix.net/{id['images']['mobile']}")


url = "https://landingfoliocom.imgix.net/inspiration/1676592912149Campsite20mobile5c4962367a4a4b11a24f4727a9d85886png"
src = requests.get(url, 'wb').content
print(src)

with open('444.png', 'wb') as file:
    file.write(src)


# print(len(data[0].get('screenshots')))
# print(data[0].get('screenshots')[0].get('images'))

# with open('111.txt', 'rb') as f:
#     req = requests.get(url_mail)
#     print(f.read().decode('utf8'))

# print(DEFAULT_CA_BUNDLE_PATH)
#
#
# with open('venv\lib\site-packages\certifi\cacert.pem', 'r') as f:
#     print(f.read())

# print(proxy_one['https'].split('@')[1].split(':')[0])
# print(headers)
# proxy_checker(url, list_proxy)
# print(get_request(url_check_ip_and_useragent, headers, proxy_one).cookies)
# print(ip_useragent_checker(headers, proxy_one))

# if not os.path.exists(f"1111"):
#     os.mkdir(f"1111")

url = 'https://httpbin.org/ip'

#
# req = requests.get(url, proxies=None, headers=None)


# s = Session()
#
# req = Request('GET', url, headers=header_1)
# prepped = req.prepare()
#
# print(prepped.headers)


# req = requests.get(url)
# print(req.request.headers)
# print(req.headers)
# print(re)

# s1 = requests.Session()
# s1.proxies.update(proxy_1)
# s1.headers.update(header_1)
# s2 = requests.session()
# s2.proxies.update(proxy_2)
# s2.headers.update(header_2)
# s3 = requests.Session()
# s3.headers.update(header_2)
#
# list_session = [s1, s2, s3]
# for item in list_org:
#     list_urls.append(f"https://vbankcenter.ru{item.find('a', class_='overlap text-blue').get('href')}")
# print(list_urls)
# start = time.time()
# count = 1
# for item in list_urls:
#     # ses = random.choice(list_session)
#     print(f"{count} - {requests.get(item)}")
#     # print(s2.proxies)
#     count += 1
# print(time.time() - start)
