## -*- coding: utf-8 -*-
import types
import telebot # type: ignore
#Получение токена из файла BotToken.py
from BotToken import Token
#Получение списка знаков зодиака из файла ZodiacSigns.py
from ZodiacSigns import ZodiacSigns
#Получение класса для Reply клавиатуры
from telebot.types import ReplyKeyboardMarkup, KeyboardButton # type: ignore
#Получение ботом токена
bot = telebot.TeleBot(Token)
#Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
	#создание клавиатуры
	main = ReplyKeyboardMarkup(resize_keyboard=True)
	#Берет строки из списка ZodiacSigns и циклом делает каждую строку
	#отдельной кнопкой
	for fd in ZodiacSigns:
		main.add(KeyboardButton(str(fd)))
	#выдача клавиатуры пользователю и вывод сообщения
	bot.reply_to(message, 'Выберите знак зодиака', reply_markup=main)












bot.infinity_polling()