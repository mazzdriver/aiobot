import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '2101241794:AAESTzO7C0hgAK8J2PyK-LwnmGq-5Oe9qJw'
ERROR_TEXT: str = 'Вот что, ребята, кота я вам не дам... (с)'
BASIC_TEXT: str = 'Я тебя не понимаю, держи кота)'
API_CATS_URL: str = 'https://aws.random.cat/meow'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int
cat_response: requests.Response
cat_link: str

while counter < MAX_COUNTER:

    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={BASIC_TEXT}')
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
