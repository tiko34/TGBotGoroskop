## -*- coding: utf-8 -*-
import telebot  # type: ignore
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
	bot.reply_to(message, 'Выберите знак зодиака', reply_markup=main)
#Обработка всех текста ботом
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
			bot.reply_to(message, 'Выберите знак зодиака', reply_markup=main)
		case 'Телец':
#создание клавиатуры для тельца
			taurus = ReplyKeyboardMarkup(resize_keyboard=True)
#Берет строки из списка DefaultButton и циклом делает каждую строку
#отдельной кнопкой
			for DB in DefaultButton:
				taurus.add(KeyboardButton(str(DB)))
			bot.reply_to(message, 'На какой день хотите получить гороскоп?', reply_markup=taurus)
#Выбор дня на выдачу гороскопа
			match message.text:
				case 'Завтра':
					bot.reply_to(message,'Извините раздел еще не готов для тельцов(')
				case 'Сегодня':
					bot.reply_to(message,'Извините раздел еще не готов для тельцов(')
#Ответ пользователю если не найдена команда
		case _:
			bot.reply_to(message,'Извините, я не знаю такой команды')













bot.infinity_polling()