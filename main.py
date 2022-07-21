import telebot

bot = telebot.TeleBot('754944002:AAH2sEJrANBaSEKLs1o51AMAvDCYw5iXZXk')

@bot.message_handler(commands=['start'])


def start_message(message):
    bot.send_message(message.chat.id, 'Send me the card name')

@bot.message_handler(content_types=['text'])


def send_text(message):
    if message.text.lower() == 'test1':
        url = 'https://api.scryfall.com/cards/e9d5aee0-5963-41db-a22b-cfea40a967a3?format=image'
        bot.send_photo(message.chat.id,url)
        #bot.send_document(message.chat.id, img)
    elif message.text.lower() == 'test2':
        url = 'https://api.scryfall.com/cards/00006596-1166-4a79-8443-ca9f82e6db4e?format=image'
        bot.send_photo(message.chat.id, url)

    else:
        bot.send_message(message.chat.id, 'Прости, но пока у меня нет этих карт')


bot.polling()


