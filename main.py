import telebot
from random import randint
from datetime import datetime
bot = telebot.TeleBot("7393376401:AAFaZT6JLWB92S3i2Xu0PowykzJ9XKsVQLc", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Привет,меня зовут ANI_bot, я бот для игр, я буду вам предлагать играть игры каждый день по одной приятного геймнинга.")
@bot.message_handler(commands=['date'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Сейчас" +str(datetime.today()))
@bot.message_handler(commands=['random'])
def send_welcome(message):
    bot.send_message(message.chat.id,"случайное число"+str(randint(1, 1000)))

bot.polling(none_stop=True, interval=0)
