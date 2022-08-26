import os

import requests
import pprint
import json
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()
print(os.environ['TOKEN'])


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    request_url = "https://api-ssl.bitly.com/v4/shorten"

    create_bitlink = {
        "long_url": url,
    }

    response = requests.post(request_url, headers=headers, json=create_bitlink)
    response.raise_for_status()

    return json.loads(response.text)['id']


def bitlink_information_from_url(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    parsed_url = urlparse(url)

    request_url = "https://api-ssl.bitly.com/v4/shorten"

    body = {
        "long_url": url,
    }

    response = requests.post(request_url, headers=headers, json=body)
    response.raise_for_status()

    return json.loads(response.text)['id']


def count_clicks(token, link):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    link_parsed = urlparse(link)

    request_link = f"{link_parsed.netloc}/{link_parsed.path}"

    request_url = f"https://api-ssl.bitly.com/v4/bitlinks/{request_link}/clicks/summary"

    response = requests.get(request_url, headers=headers)
    response.raise_for_status()

    return json.loads(response.text)['total_clicks']


def is_bitlink(url):
    url_parsed = urlparse(url)
    print(url, url_parsed)
    if url_parsed.netloc == 'bit.ly':
        return True

    return False


url = input()

if is_bitlink(url):
    try:
        total_clicks = count_clicks(TOKEN, url)
        print(total_clicks)
    except requests.exceptions.HTTPError as error:
        exit(f"Не могу получить кол-во кликов по причине: {error}")
else:
    try:
        shorten_link = shorten_link(TOKEN, url)
        print(shorten_link)
    except requests.exceptions.HTTPError as error:
        exit(f"Не могу получить информацию по ссылке по причине: {error}")
