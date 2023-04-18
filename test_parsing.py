from proxy_list import *

list_proxy = create_proxy_list('datapool/proxy.txt')
proxy_one = proxy_for_request(list_proxy[1])
user_agents_list = create_useragent_list('datapool/user_agents_decktop.txt')
headers = {"user-agent": f"{user_agents_list[100]}"}
url_check_https = 'https://2ip.ru/'
url_check_http = 'http://checkip.dyndns.org'
url = 'https://vbankcenter.ru/contragent/1145256007577'
url_proxy = 'https://proxy6.net'
url_mail = 'https://mail.ru/'
url_kinosal = 'https://forum.kinozal.me/index.php'
url_check_useragent = 'https://ciox.ru/check-user-agent'
url_check_ip_and_useragent = 'https://tools.browsernative.com/'

print(list_proxy)
print(user_agents_list[0])

# proxy_checker(url, list_proxy)
# print(get_request(url_check_ip_and_useragent, headers, proxy_one).text)
# print(ip_useragent_checker(headers, proxy_one))
