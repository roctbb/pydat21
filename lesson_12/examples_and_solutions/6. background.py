import time

import telebot
import threading
import requests

token = "1746449420:AAHqX5xvNsdjj2KKnjByGKr9f9SkNW9SCbk"

bot = telebot.TeleBot(token=token)
users = set()

def get_price():
    answer = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    return answer.json()["bpi"]["USD"]["rate"]

def mailing():
    while True:
        print("start mailing", users)
        current_price = get_price()

        for user in users:
            bot.send_message(user, "Текущая цена Bitcoin = {}$".format(current_price))

        time.sleep(5)

@bot.message_handler(commands=['price'])
def price(message):
    bot.send_message(message.chat.id, "Текущая цена Bitcoin = {}$".format(get_price()))


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    users.add(message.chat.id)

@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    try:
        users.discard(message.chat.id)
    except:
        pass

thread = threading.Thread(target=mailing)
thread.start()

while True:
    try:
        bot.polling(none_stop=True)
    except:
        pass


