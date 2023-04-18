import requests


def create_proxy_list(file_data):
    with open(file_data, 'r') as file:
        return file.read().split()


def proxy_for_request(proxy_string):
    return {
        "http": f"http://{proxy_string}",
        "https": f"http://{proxy_string}",
    }


def proxy_checker(url, list_proxy):
    url_checker_non_proxy(url)
    for item in list_proxy:
        req = ''
        try:
            req = requests.get(url, proxies=proxy_for_request(item), timeout=5)
            print(f"{url} - {req} - {item.split('@')[1]}")
        except Exception:
            print(f"ERROR: {url} - {req} - {item.split('@')[1]}")


def url_checker_non_proxy(url):
    req = ''
    try:
        req = requests.get(url, timeout=5)
        print(f"{url} - {req} - No proxy")
    except Exception:
        print(f"ERROR: {url} - No proxy")
