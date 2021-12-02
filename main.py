import telebot

bot = telebot.TeleBot('754944002:AAH2sEJrANBaSEKLs1o51AMAvDCYw5iXZXk')

@bot.message_handler(commands=['start'])


def start_message(message):
    bot.send_message(message.chat.id, 'Send me the card name')

@bot.message_handler(content_types=['text'])


def send_text(message):
    if message.text.lower() == 'прости':
        url = 'https://api.scryfall.com/cards/e9d5aee0-5963-41db-a22b-cfea40a967a3?format=image'
        #img = Image.open(urlopen(url))


        bot.send_photo(message.chat.id,url)
        #bot.send_document(message.chat.id, img)
   # elif message.text.lower() == 'наш второй смайлик':
    #    img = open('Смайлики и люди 2.png', 'rb')
     #   bot.send_document(message.chat.id, img)

    else:
        bot.send_message(message.chat.id, 'Прости, но пока у меня нет этих Emoji')


bot.polling()


