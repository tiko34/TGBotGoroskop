## -*- coding: utf-8 -*-

import aiogram
import asyncio
import aiogram.fsm
import aiogram.fsm.storage
import aiogram.fsm.storage.memory
#Получение токена из файла BotToken.py
from Privat_Strings import TOKEN
#Функция для парсинга страниц
from Parsing import parsing_site
# #Получение списка знаков зодиака из файла ZodiacSigns.py
from ZodiacSignsList import ZodiacSigns
# #Получение базовых кнопок из файла DefaultButtonList.py
from DefaultButtonList import DefaultButton
#Эмодзи 
# from Emoji import Emojiwarning,Emojismile_cat
# #Получение классов для Reply клавиатуры
from telebot.types import ReplyKeyboardMarkup, KeyboardButton # type: ignore
from telebot.async_telebot import AsyncTeleBot


#Получение ботом токена
bot = AsyncTeleBot(TOKEN)
storage = aiogram.fsm.storage.memory.MemoryStorage()
dp = aiogram.Dispatcher()

# Определение состояний
@dp.message_handler
class Form(aiogram.StatesGroup):
    waiting_for_day = State()
    #waiting_for_age = State()




#Обработка команды /start
@bot.message_handler(commands=['start'])
async def send_welcome(message):
#Осведомление пользователя о времени обновления гороскопа
	await bot.send_message(message.chat.id, '\U000026A0'+'ВАЖНО!'+'\U000026A0'+'\nГороскоп обновляется по МСК')
	await zodiac_keboard(message)
#Получение набора клавиатуры со знаками зодиака
	



# #Обработка всего текста ботом
@bot.message_handler(content_types=['text'])
async def user_message(message):
	match message.text:
		case 'Меню':
			await zodiac_keboard(message)
		case 'Телец':
			await default_keboard(message)
			await taurus_days_selection(message)
			#await bot.register_next_step_handler(message, taurus_days_selection)
		case 'Овен':
			await default_keboard(message)
			await bot.register_next_step_handler(message, aries_days_selection)
		case 'Близнецы':
			await default_keboard(message)
			await bot.register_next_step_handler(message, gemini_days_selection)
		case 'Рак':
			await default_keboard(message)
			await bot.register_next_step_handler(message, cancer_days_selection)
		case 'Лев':
			await default_keboard(message)
			await bot.register_next_step_handler(message, leo_days_selection)
		case 'Дева':
			await default_keboard(message)
			await bot.register_next_step_handler(message, virgo_days_selection)
		case 'Весы':
			await default_keboard(message)
			await bot.register_next_step_handler(message, libra_days_selection)
		case 'Скорпион':
			await default_keboard(message)
			await bot.register_next_step_handler(message, scorpio_days_selection)
		case 'Стрелец':
			await default_keboard(message)
			await bot.register_next_step_handler(message, sagittarius_days_selection)
		case 'Козерог':
			await default_keboard(message)
			await bot.register_next_step_handler(message, capricorn_days_selection)
		case 'Водолей':
			await default_keboard(message)
			await bot.register_next_step_handler(message, aquarius_days_selection)
		case 'Рыбы':
			await default_keboard(message)
			await bot.register_next_step_handler(message, pisces_days_selection)

#Функции для создания наборов клавиатур
async def default_keboard(message):
#создание клавиатуры 
			defaultkeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#Берет строки из списка DefaultButton и циклом делает каждую строку
#отдельной кнопкой
			for DB in DefaultButton:
				defaultkeyboard.add(KeyboardButton(str(DB)))
			await bot.send_message(message.chat.id, 'На какой день хотите получить гороскоп?', reply_markup=defaultkeyboard)
async def zodiac_keboard(message):
#создание стартовой клавиатуры
			zodiac_keboard = ReplyKeyboardMarkup(resize_keyboard=True)
#Берет строки из списка ZodiacSigns и циклом делает каждую строку
#отдельной кнопкой
			for ZS in ZodiacSigns:
				zodiac_keboard.add(KeyboardButton(str(ZS)))
#выдача клавиатуры пользователю и вывод сообщения
			await bot.send_message(message.chat.id, '\U0001F63A'+'Выберите знак зодиака'+'\U0001F63A', reply_markup=zodiac_keboard)

# #Функции для действий с конкретным знаком зодиака
async def taurus_days_selection(message):
		result = dp.feed_update(bot=bot, update=message)
		match message.text:
			case 'Завтра':
				temp = parsing_site('taurus','tomorrow')
				for data in temp:
					bot.send_message(message.chat.id,data.string)
				await bot.register_next_step_handler(message, taurus_days_selection)
			case 'Меню':
				await zodiac_keboard(message)
			case 'Сегодня':
				temp = parsing_site('taurus','today')
				for data in temp:
					bot.send_message(message.chat.id,data.string)		
				await bot.register_next_step_handler(message, taurus_days_selection)
def aries_days_selection(message):
	
	match message.text:
		case 'Завтра':
			temp = parsing_site('aries','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)		
			bot.register_next_step_handler(message, aries_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('aries','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)		
			bot.register_next_step_handler(message, aries_days_selection)
async def gemini_days_selection(message):
	
	match message.text:
		case 'Завтра':
			temp = parsing_site('gemini','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, gemini_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('gemini','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, gemini_days_selection)
def cancer_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('cancer','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, cancer_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('cancer','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, cancer_days_selection)
def leo_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('leo','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, leo_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('leo','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, leo_days_selection)
def virgo_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('virgo','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, virgo_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('virgo','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, virgo_days_selection)
def libra_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('libra','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, libra_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('libra','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, libra_days_selection)
def scorpio_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('scorpio','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, scorpio_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('scorpio','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, scorpio_days_selection)
def sagittarius_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('sagittarius','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, sagittarius_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('sagittarius','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, sagittarius_days_selection)
def capricorn_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('capricorn','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, capricorn_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('capricorn','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, capricorn_days_selection)
def aquarius_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('aquarius','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, aquarius_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('aquarius','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, aquarius_days_selection)
def pisces_days_selection(message):
	match message.text:
		case 'Завтра':
			temp = parsing_site('pisces','tomorrow')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, pisces_days_selection)
		case 'Меню':
			zodiac_keboard(message)
		case 'Сегодня':
			temp = parsing_site('pisces','today')
			for data in temp:
				bot.send_message(message.chat.id,data.string)
			bot.register_next_step_handler(message, pisces_days_selection)



# Функция для запуска бота
async def main():
    await bot.infinity_polling()

asyncio.run(main())
