import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '2101241794:AAESTzO7C0hgAK8J2PyK-LwnmGq-5Oe9qJw'
offset: int = -2
timeout: int = 0
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
