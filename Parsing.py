## -*- coding: utf-8 -*-
import requests # type: ignore
#Библиотека для парсинга
from bs4 import BeautifulSoup # type: ignore

global url
url='https://horo.mail.ru/prediction/'

session = requests.Session()

zodiac_cache = {}

def parsing_site(zodiac, day):
    """
    Функция парсинга данных с использованием кеша, который обновляется раз в сутки.
    :param zodiac: Название знака зодиака (например, "taurus", "aries").
    :param day: День, для которого нужно получить данные (например, "today", "tomorrow").
    :return: Список строк с данными гороскопа или сообщение об ошибке.
    """
    import datetime  # Импорт модуля для работы с датами

    # Получаем текущую дату в формате yyyy-mm-dd (например, "2025-01-01")
    today = datetime.date.today()

    # Генерируем уникальный ключ для кеша на основе знака зодиака и дня
    # Например, для "taurus" и "today" ключ будет "taurus_today"
    cache_key = f"{zodiac}_{day}"

    # Проверяем, есть ли данные в кеше и совпадает ли дата кеша с сегодняшней
    if cache_key in zodiac_cache:
        cache_data = zodiac_cache[cache_key]  # Получаем данные из кеша
        if cache_data["date"] == today:  # Проверяем, соответствует ли кеш текущей дате
            return cache_data["data"]  # Возвращаем данные из кеша, если они актуальны

    # Если данных нет в кеше или они устарели, выполняем HTTP-запрос
    try:
        # Формируем URL для запроса данных гороскопа
        # Например, https://horo.mail.ru/prediction/taurus/today/
        correct_url = f"{url}{zodiac}/{day}/"

        # Выполняем GET-запрос к серверу с установленным таймаутом 10 секунд
        response = session.get(correct_url, timeout=10)

        # Проверяем статус ответа. Если статус-код не 200, выбрасывается исключение
        response.raise_for_status()

        # Парсим HTML-код страницы с помощью BeautifulSoup
        bs = BeautifulSoup(response.text, 'lxml')

        # Инициализируем список для хранения результатов парсинга
        result = []  

        # Ищем первый элемент с определённым классом (например, основное предсказание)
        # Добавляем его текст в результат (strip=True удаляет лишние пробелы)
        result += [span.get_text(strip=True) for span in bs.find_all('span', class_='f2eee589ba c6eb8d9a4c', limit=1)]

        # Ищем дополнительный элемент с другим классом (например, советы)
        result += [span.get_text(strip=True) for span in bs.find_all('span', class_='f2eee589ba cd39273477 e1df578fc6 e53e657292 a7a6fb85f2', limit=1)]

        # Ищем текстовые абзацы (ограничиваем количество найденных элементов до 5)
        result += [p.get_text(strip=True) for p in bs.find_all('p', limit=5)]

        # Сохраняем результаты в кеш с текущей датой
        # Кеш состоит из данных парсинга и даты их сохранения
        zodiac_cache[cache_key] = {"data": result, "date": today}

        # Возвращаем список результатов парсинга
        return result

    # Обработка ошибок HTTP-запроса, например, таймаутов или недоступности сайта
    except requests.exceptions.RequestException as e:
        # Возвращаем сообщение об ошибке
        return [f"Ошибка запроса: {str(e)}"]

    # Общая обработка других исключений, например, ошибок парсинга
    except Exception as e:
        # Возвращаем сообщение об ошибке парсинга
        return [f"Ошибка парсинга: {str(e)}"]


# Словарь для кеширования списка знаков зодиака
zodiac_list_cache = {}

def parsing_site_zodiac_List():
    """
    Функция парсинга списка знаков зодиака с использованием кеша.
    :return: Список названий знаков зодиака или сообщение об ошибке.
    """
    # Проверяем, есть ли данные в кеше
    if "zodiac_list" in zodiac_list_cache:
        # Если данные есть, возвращаем их из кеша
        return zodiac_list_cache["zodiac_list"]

    try:
        # Формируем URL для страницы с полным списком знаков зодиака
        # Например, https://horo.mail.ru/prediction/tomorrow/
        url_zodiac_list = f"{url}tomorrow/"

        # Выполняем GET-запрос к серверу с таймаутом 5 секунд
        response = session.get(url_zodiac_list, timeout=5)

        # Проверяем статус ответа. Если статус-код не 200, выбрасывается исключение
        response.raise_for_status()

        # Парсим HTML-код страницы с помощью BeautifulSoup
        bs = BeautifulSoup(response.text, 'lxml')

        # Извлекаем список знаков зодиака из найденных элементов
        # find_all ищет элементы с указанным классом, а text извлекает их текстовое содержимое
        # limit=12 ограничивает количество найденных элементов до 12
        result = [elem.text for elem in bs.find_all(class_='da2727fca3 b40b56773d e65bdf6865', limit=12)]

        # Сохраняем результат в кеш для последующего использования
        zodiac_list_cache["zodiac_list"] = result

        # Возвращаем список названий знаков зодиака
        return result

    # Обработка ошибок HTTP-запроса
    except requests.exceptions.RequestException as e:
        # Возвращаем сообщение об ошибке запроса
        return [f"Ошибка запроса: {str(e)}"]

    # Обработка других исключений (например, ошибок парсинга)
    except Exception as e:
        # Возвращаем сообщение об ошибке парсинга
        return [f"Ошибка парсинга: {str(e)}"]

	    



		