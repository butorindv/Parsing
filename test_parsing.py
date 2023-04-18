from proxy_list import create_proxy_list
from proxy_list import proxy_checker

list_proxy = create_proxy_list('datapool/proxy.txt')
url_check_https = 'https://2ip.ru/'
url_check_http = 'http://checkip.dyndns.org'
url = 'https://vbankcenter.ru/contragent/1145256007577'
url_proxy = 'https://proxy6.net'
url_mail = 'https://mail.ru/'
url_kinosal = 'https://forum.kinozal.me/index.php'

proxy_checker(url, list_proxy)
