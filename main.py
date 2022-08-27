import os
import requests
import json
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['TOKEN']


def shorten_link(long_url):
    headers = {
        'Authorization': f'Bearer {TOKEN}',
    }

    request_url = "https://api-ssl.bitly.com/v4/shorten"

    long_url_json = {
        "long_url": long_url,
    }

    response = requests.post(request_url, headers=headers, json=long_url_json)
    response.raise_for_status()

    return json.loads(response.text)['id']


def count_clicks(link):
    headers = {
        'Authorization': f'Bearer {TOKEN}',
    }

    link_parsed = urlparse(link)

    request_link = f"{link_parsed.netloc}/{link_parsed.path}"

    request_url = f"https://api-ssl.bitly.com/v4/bitlinks/{request_link}/clicks/summary"

    response = requests.get(request_url, headers=headers)
    response.raise_for_status()

    return json.loads(response.text)['total_clicks']


def is_bitlink(input_url):
    url_parsed = urlparse(input_url)
    if url_parsed.netloc == 'bit.ly':
        return True
    return False


if __name__ == '__main__':
    url = input()

    if is_bitlink(url):
        try:
            total_clicks = count_clicks(url)
            print(f"Всего кликов: {total_clicks}")
        except requests.exceptions.HTTPError as error:
            exit(f"Не могу получить кол-во кликов по причине: {error}")
    else:
        try:
            shorten_link = shorten_link(url)
            print(f"Битлинк: {shorten_link}")
        except requests.exceptions.HTTPError as error:
            exit(f"Не могу получить информацию по ссылке по причине: {error}")
