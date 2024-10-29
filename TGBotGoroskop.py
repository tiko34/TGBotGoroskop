## -*- coding: utf-8 -*-
#библиотека для телеграмм бота
import telebot  # type: ignore
#Библиотека для отправления и получения запросов от сайтов в интернете
import requests # type: ignore
#Библиотека для парсинга
from bs4 import BeautifulSoup # type: ignore
#Получение токена из файла BotToken.py
from BotToken import Token
#Получение списка знаков зодиака из файла ZodiacSigns.py
from ZodiacSignsList import ZodiacSigns
#Получение базовых двух кнопок из файла DefaultButtonList.py
from DefaultButtonList import DefaultButton
#Получение класса для Reply клавиатуры
from telebot.types import ReplyKeyboardMarkup, KeyboardButton # type: ignore
#Получение ботом токена
bot = telebot.TeleBot(Token)
#Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
	#создание стартовой клавиатуры
	main = ReplyKeyboardMarkup(resize_keyboard=True)
	#Берет строки из списка ZodiacSigns и циклом делает каждую строку
	#отдельной кнопкой
	for ZS in ZodiacSigns:
		main.add(KeyboardButton(str(ZS)))
	#выдача клавиатуры пользователю и вывод сообщения
	bot.send_message(message.chat.id, 'Выберите знак зодиака', reply_markup=main)
#Обработка всего текста ботом
@bot.message_handler(content_types=['text'])
def user_message(message):
#Case для обработки всего текста поступающего боту
	match message.text:
		case 'Главное меню':
#создание стартовой клавиатуры
			main = ReplyKeyboardMarkup(resize_keyboard=True)
#Берет строки из списка ZodiacSigns и циклом делает каждую строку
#отдельной кнопкой
			for ZS in ZodiacSigns:
				main.add(KeyboardButton(str(ZS)))
#выдача клавиатуры пользователю и вывод сообщения
			bot.send_message(message.chat.id, 'Выберите знак зодиака', reply_markup=main)
		case 'Телец':
#создание клавиатуры для тельца
			taurus = ReplyKeyboardMarkup(resize_keyboard=True)
#Берет строки из списка DefaultButton и циклом делает каждую строку
#отдельной кнопкой
			for DB in DefaultButton:
				taurus.add(KeyboardButton(str(DB)))
			bot.send_message(message.chat.id, 'На какой день хотите получить гороскоп?', reply_markup=taurus)

#Переход к функции taurus_days_selection для выбора дальнешего действия
			bot.register_next_step_handler(message, taurus_days_selection)


def taurus_days_selection(message):

	match message.text:
		case 'Завтра':
			url='https://horo.mail.ru/prediction/taurus/tomorrow/'
			response = requests.get(url)
			bs = BeautifulSoup(response.text,'lxml')
			temp = bs.findAll('p')
			for data in temp:
				bot.send_message(message.chat.id,data)			
		case 'Сегодня':
			url='https://horo.mail.ru/prediction/taurus/today/'
			response = requests.get(url)
			bs = BeautifulSoup(response.text,"lxml")
			temp = bs.findAll('p')
			for data in temp:
				bot.send_message(message.chat.id,data)		





			














bot.infinity_polling()