## -*- coding: utf-8 -*-
#библиотека для телеграмм бота
import telebot  # type: ignore
#Получение токена из файла BotToken.py
from BotToken import Token
#Функция для парсинга страниц
from Parsing import parsing_site
#Получение списка знаков зодиака из файла ZodiacSigns.py
from ZodiacSignsList import ZodiacSigns
#Получение базовых кнопок из файла DefaultButtonList.py
from DefaultButtonList import DefaultButton
#Эмодзи 
from Emoji import warning,smile_cat
#Получение классов для Reply клавиатуры
from telebot.types import ReplyKeyboardMarkup, KeyboardButton # type: ignore
#Получение ботом токена
bot = telebot.TeleBot(Token)

#Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
#Осведомление пользователя о времени обновления гороскопа
	bot.send_message(message.chat.id, warning+'ВАЖНО!'+warning+'\nГороскоп обновляется по МСК')
#Получение набора клавиатуры со знаками зодиака
	zodiac_keboard(message)

#Обработка всего текста ботом
@bot.message_handler(content_types=['text'])
def user_message(message):
	match message.text:
		case 'Меню':
			zodiac_keboard(message)
		case 'Телец':
			default_keboard(message)
			bot.register_next_step_handler(message, taurus_days_selection)
		case 'Овен':
			default_keboard(message)
			bot.register_next_step_handler(message, aries_days_selection)
		case 'Близнецы':
			default_keboard(message)
			bot.register_next_step_handler(message, gemini_days_selection)
		case 'Рак':
			default_keboard(message)
			bot.register_next_step_handler(message, cancer_days_selection)
		case 'Лев':
			default_keboard(message)
			bot.register_next_step_handler(message, leo_days_selection)
		case 'Дева':
			default_keboard(message)
			bot.register_next_step_handler(message, virgo_days_selection)
		case 'Весы':
			default_keboard(message)
			bot.register_next_step_handler(message, libra_days_selection)
		case 'Скорпион':
			default_keboard(message)
			bot.register_next_step_handler(message, scorpio_days_selection)
		case 'Стрелец':
			default_keboard(message)
			bot.register_next_step_handler(message, sagittarius_days_selection)
		case 'Козерог':
			default_keboard(message)
			bot.register_next_step_handler(message, capricorn_days_selection)
		case 'Водолей':
			default_keboard(message)
			bot.register_next_step_handler(message, aquarius_days_selection)
		case 'Рыбы':
			default_keboard(message)
			bot.register_next_step_handler(message, pisces_days_selection)

#Функции для создания наборов клавиатур
def default_keboard(message):
#создание клавиатуры 
			defaultkeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#Берет строки из списка DefaultButton и циклом делает каждую строку
#отдельной кнопкой
			for DB in DefaultButton:
				defaultkeyboard.add(KeyboardButton(str(DB)))
			bot.send_message(message.chat.id, 'На какой день хотите получить гороскоп?', reply_markup=defaultkeyboard)
def zodiac_keboard(message):
#создание стартовой клавиатуры
			zodiac_keboard = ReplyKeyboardMarkup(resize_keyboard=True)
#Берет строки из списка ZodiacSigns и циклом делает каждую строку
#отдельной кнопкой
			for ZS in ZodiacSigns:
				zodiac_keboard.add(KeyboardButton(str(ZS)))
#выдача клавиатуры пользователю и вывод сообщения
			bot.send_message(message.chat.id, smile_cat+'Выберите знак зодиака'+smile_cat, reply_markup=zodiac_keboard)

#Функции для действий с конкретным знаком зодиака
def taurus_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('taurus','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)	
			bot.register_next_step_handler(message, taurus_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('taurus','today')
			for data in temp:
				bot.send_message(message.chat.id,data)		
			bot.register_next_step_handler(message, taurus_days_selection)
def aries_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('aries','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)		
			bot.register_next_step_handler(message, aries_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('aries','today')
			for data in temp:
				bot.send_message(message.chat.id,data)		
			bot.register_next_step_handler(message, aries_days_selection)
def gemini_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('gemini','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, gemini_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('gemini','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, gemini_days_selection)
def cancer_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('cancer','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, cancer_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('cancer','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, cancer_days_selection)
def leo_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('leo','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, leo_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('leo','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, leo_days_selection)
def virgo_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('virgo','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, virgo_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('virgo','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, virgo_days_selection)
def libra_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('libra','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, libra_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('libra','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, libra_days_selection)
def scorpio_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('scorpio','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, scorpio_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('scorpio','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, scorpio_days_selection)
def sagittarius_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('sagittarius','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, sagittarius_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('sagittarius','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, sagittarius_days_selection)
def capricorn_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('capricorn','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, capricorn_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('capricorn','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, capricorn_days_selection)
def aquarius_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('aquarius','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, aquarius_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('aquarius','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, aquarius_days_selection)
def pisces_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('pisces','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, pisces_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('pisces','today')
			for data in temp:
				bot.send_message(message.chat.id,data)
			bot.register_next_step_handler(message, pisces_days_selection)

try:
	print('Телеграмм бот успешно запущен')
	bot.infinity_polling()
except Exception as err:
    print('Ошибка при старте:'+err)
