import telebot
import random
import os
from telebot import types
TOKEN = '5672099416:AAF6_9fju-tVMRR3JXOEDp0lcQHIIsSOMkM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Музыка 🫀')
    markup.add(item1)
    bot.send_audio(m.chat.id, open('./files/audio/loveyou.ogg', 'rb'), reply_markup=markup)

@bot.message_handler(content_types= ['text'])
def bot_message(m):
    if m.chat.type == 'private':
        if m.text == 'Музыка 🫀':
            random_audio = random.choice(os.listdir("./files/audio/"))
            random_photo = random.choice(os.listdir("./files/photos/"))
            bot.send_photo(m.chat.id, open('./files/photos/' + random_photo, 'rb'))
            bot.send_audio(m.chat.id, open('./files/audio/' + random_audio, 'rb'))


bot.polling(none_stop=True, interval=0)