import telebot
import random

token = "1746449420:AAGVg7QrulkojNCFd-umFv0rT0V75BZr8wo"

bot = telebot.TeleBot(token=token)
aneks = ["Купил мужик шляпу, а она ему как раз...", "Колобок повесился"]

@bot.message_handler(commands=['anek'])
def get_anek(message):
    bot.send_message(message.chat.id, random.choice(aneks))

@bot.message_handler(commands=['start', 'help'])
def get_help(message):
    bot.send_message(message.chat.id, "Напиши /anek")

@bot.message_handler(content_types=['text'])
def get_text(message):
    bot.send_message(message.chat.id, "Я тебя не понимаю")

bot.polling(none_stop=True)