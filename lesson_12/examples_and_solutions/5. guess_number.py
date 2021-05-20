import telebot
import random

token = "1746449420:AAHqX5xvNsdjj2KKnjByGKr9f9SkNW9SCbk"

bot = telebot.TeleBot(token=token)
numbers = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    numbers[user_id] = random.randint(1, 100)
    bot.send_message(user_id, "Я загадал число. Попробуйте отгадать?")

@bot.message_handler(content_types=['text'])
def guess(message):
    user_id = message.chat.id
    try:
        number = int(message.text)

        if number > 100:
            bot.send_message(user_id, "Число меньше 101.")
        elif number <= 0:
            bot.send_message(user_id, "Число больше 0.")
        else:
            guessed_number = numbers[user_id]

            if number < guessed_number:
                bot.send_message(user_id, "Маловато.")
            elif number > guessed_number:
                bot.send_message(user_id, "Многовато.")
            else:
                bot.send_message(user_id, "Вы отгадали! Загадываю новое число!")
                numbers[user_id] = random.randint(1, 100)

    except:
        bot.send_message(user_id, "Введите число.")

bot.polling(none_stop=True)