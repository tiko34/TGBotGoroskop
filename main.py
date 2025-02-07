## -*- coding: utf-8 -*-
import traceback
import os
import telebot  # type: ignore
#Функция для парсинга страниц
from Parsing import parsing_site,parsing_site_zodiac_List
#Эмодзи 
from Emoji import warning,smile_cat
#Получение Токена бота 
#from Config import TOKEN
<<<<<<< HEAD
# Получаем токен из переменной среды
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
=======
>>>>>>> master
#Получение классов для Reply клавиатуры
from telebot.types import ReplyKeyboardMarkup, KeyboardButton # type: ignore
#Получение ботом токена
bot = telebot.TeleBot(TOKEN)

def create_keyboard(options):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for option in options:
        keyboard.add(KeyboardButton(str(option)))
    return keyboard

def default_keyboard(message):
    bot.send_message(message.chat.id, 'На какой день хотите получить гороскоп?', 
                     reply_markup=create_keyboard(['Сегодня', 'Завтра', 'Меню']))

def zodiac_keyboard(message):
    bot.send_message(message.chat.id, f'{smile_cat}Выберите знак зодиака{smile_cat}', 
                     reply_markup=create_keyboard(parsing_site_zodiac_List()))

#Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
#Осведомление пользователя о времени обновления гороскопа
	bot.send_message(message.chat.id, warning+'ВАЖНО!'+warning+'\nГороскоп обновляется по МСК')
#Получение набора клавиатуры со знаками зодиака
	zodiac_keyboard(message)

@bot.message_handler(content_types=['text'])
def user_message(message):
    handlers = {
        'Меню': lambda msg: zodiac_keyboard(msg),
        'Телец': lambda msg: handle_zodiac(msg, taurus_days_selection),
        'Овен': lambda msg: handle_zodiac(msg, aries_days_selection),
        'Близнецы': lambda msg: handle_zodiac(msg, gemini_days_selection),
        'Рак': lambda msg: handle_zodiac(msg, cancer_days_selection),
        'Лев': lambda msg: handle_zodiac(msg, leo_days_selection),
        'Дева': lambda msg: handle_zodiac(msg, virgo_days_selection),
        'Весы': lambda msg: handle_zodiac(msg, libra_days_selection),
        'Скорпион': lambda msg: handle_zodiac(msg, scorpio_days_selection),
        'Стрелец': lambda msg: handle_zodiac(msg, sagittarius_days_selection),
        'Козерог': lambda msg: handle_zodiac(msg, capricorn_days_selection),
        'Водолей': lambda msg: handle_zodiac(msg, aquarius_days_selection),
        'Рыбы': lambda msg: handle_zodiac(msg, pisces_days_selection),
    }

    handler = handlers.get(message.text)
    if handler:
        handler(message)
    else:
        bot.send_message(message.chat.id, "Команда не распознана. Пожалуйста, выберите из предложенных вариантов.")

def handle_zodiac(message, next_step_handler):
    default_keyboard(message)
    bot.register_next_step_handler(message, next_step_handler)

#Функции для действий с конкретным знаком зодиака
def days_selection(message, zodiac, next_step_handler):
    
   # Обработчик дней для знаков зодиака.

    match message.text:
        case 'Сегодня':
            data = parsing_site(zodiac, 'today')
        case 'Завтра':
            data = parsing_site(zodiac, 'tomorrow')
        case 'Меню':
            zodiac_keyboard(message)
            return
        case _:
            bot.send_message(message.chat.id, "Команда не распознана.")
            return
    for item in data:
        bot.send_message(message.chat.id, item)
    
    # Регистрация следующего шага
    bot.register_next_step_handler(message, next_step_handler)
# Определяем обработчики для каждого знака зодиака, передавая соответствующие параметры

def taurus_days_selection(message):
    days_selection(message, 'taurus', taurus_days_selection)

def aries_days_selection(message):
    days_selection(message, 'aries', aries_days_selection)

def gemini_days_selection(message):
    days_selection(message, 'gemini', gemini_days_selection)

def cancer_days_selection(message):
    days_selection(message, 'cancer', cancer_days_selection)

def leo_days_selection(message):
    days_selection(message, 'leo', leo_days_selection)

def virgo_days_selection(message):
    days_selection(message, 'virgo', virgo_days_selection)

def libra_days_selection(message):
    days_selection(message, 'libra', libra_days_selection)

def scorpio_days_selection(message):
    days_selection(message, 'scorpio', scorpio_days_selection)

def sagittarius_days_selection(message):
    days_selection(message, 'sagittarius', sagittarius_days_selection)

def capricorn_days_selection(message):
    days_selection(message, 'capricorn', capricorn_days_selection)

def aquarius_days_selection(message):
    days_selection(message, 'aquarius', aquarius_days_selection)

def pisces_days_selection(message):
    days_selection(message, 'pisces', pisces_days_selection)

try:
    print('Телеграмм бот успешно запущен')
    bot.infinity_polling()
except Exception as err:
    print(f'Ошибка при старте: {err}')
    traceback.print_exc()  
