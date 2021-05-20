import telebot

token = ""

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)
messages = {}

@bot.message_handler(commands=['remind'])
def remind(message):
    if message.chat.id not in messages:
        bot.send_message(message.chat.id, "Я все забыл(")
    else:
        bot.send_message(message.chat.id, messages[message.chat.id])

@bot.message_handler(content_types=['text'])
def remember(message):
    messages[message.chat.id] = message.text
    bot.send_message(message.chat.id, "Запомнил!")
    print(messages)

bot.polling(none_stop=True)