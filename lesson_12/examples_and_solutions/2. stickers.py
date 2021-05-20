import telebot
import random

token = "1746449420:AAGVg7QrulkojNCFd-umFv0rT0V75BZr8wo"

bot = telebot.TeleBot(token=token)
stickers = []

@bot.message_handler(content_types=['sticker'])
def save_sticker(message):
    stickers.append(message.sticker.file_id)

    user = message.chat.id
    random_sticker = random.choice(stickers)

    bot.send_sticker(user, random_sticker)

bot.polling(none_stop=True)