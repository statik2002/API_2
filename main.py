import os
import requests
import json
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, long_url):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    request_url = "https://api-ssl.bitly.com/v4/shorten"

    request_data = {
        "long_url": long_url,
    }

    response = requests.post(request_url, headers=headers, json=request_data)
    response.raise_for_status()

    return response.json()['id']


def count_clicks(token, link):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    parsed_link = urlparse(link)

    request_link = f"{parsed_link.netloc}/{parsed_link.path}"

    request_url = f"https://api-ssl.bitly.com/v4/bitlinks/{request_link}/clicks/summary"

    response = requests.get(request_url, headers=headers)
    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(token, input_url):

    headers = {
        'Authorization': f'Bearer {token}',
    }

    parsed_url = urlparse(input_url)

    request_link = f"{parsed_url.netloc}/{parsed_url.path}"
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{request_link}'

    response = requests.get(request_url, headers=headers)
    response.raise_for_status()

    return True


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']

    url = input('Введите ссылку: ')

    try:
        if is_bitlink(token, url):
            total_clicks = count_clicks(token, url)
            print(f"По вашей ссылке прошли : {total_clicks} раз(а)")
        else:
            short_link = shorten_link(token, url)
            print(f"Битлинк: {short_link}")

    except requests.exceptions.HTTPError as error:
        print(f"Не могу получить кол-во кликов по причине: {error}")


if __name__ == '__main__':

    main()

