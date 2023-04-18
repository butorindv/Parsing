import requests


# Функция читает файл с прокси-серверами (file_data) и возвращает список серверов
def create_proxy_list(file_data):
    with open(file_data, 'r') as file:
        return file.read().split()


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
        except Exception:
            print(f"ERROR: {url} - {req} - {item.split('@')[1]}")


# проверка сайта без прокси
def url_checker_non_proxy(url):
    req = ''
    try:
        req = requests.get(url, timeout=5)
        print(f"{url} - {req} - No proxy")
    except Exception:
        print(f"ERROR: {url} - No proxy")
