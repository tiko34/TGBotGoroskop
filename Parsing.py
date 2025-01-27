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
    """
    import datetime

    # Текущая дата (например, "2025-01-01")
    today = datetime.date.today()

    # Ключ для кеша (уникален для каждого знака и дня)
    cache_key = f"{zodiac}_{day}"

    # Проверяем, есть ли данные в кеше и совпадает ли дата кеша с сегодняшней
    if cache_key in zodiac_cache:
        cache_data = zodiac_cache[cache_key]
        if cache_data["date"] == today:
            return cache_data["data"]  # Возвращаем кеш, если дата совпадает

    # Если кеш отсутствует или устарел, делаем новый запрос
    try:
        correct_url = f"{url}{zodiac}/{day}/"
        response = session.get(correct_url, timeout=10)
        response.raise_for_status()
        bs = BeautifulSoup(response.text, 'lxml')
        result = []  
        # Используем find_all с ограничением на количество элементов для повышения скорости
        result += [span.get_text(strip=True) for span in bs.find_all('span', class_='f2eee589ba c6eb8d9a4c', limit=1)]
        result += [span.get_text(strip=True) for span in bs.find_all('span', class_='f2eee589ba cd39273477 e1df578fc6 e53e657292 a7a6fb85f2', limit=1)]
        result += [p.get_text(strip=True) for p in bs.find_all('p', limit=5)]

        # Обновляем кеш с новой датой
        zodiac_cache[cache_key] = {"data": result, "date": today}
        return result
    except requests.exceptions.RequestException as e:
        return [f"Ошибка запроса: {str(e)}"]
    except Exception as e:
        return [f"Ошибка парсинга: {str(e)}"]

#Для кеширования списка знаков зодиака
zodiac_list_cache = {}
def parsing_site_zodiac_List():
    if "zodiac_list" in zodiac_list_cache:
        return zodiac_list_cache["zodiac_list"]
    
    try:
        url_zodiac_list = f"{url}tomorrow/"
        response = session.get(url_zodiac_list, timeout=5)
        response.raise_for_status()
        bs = BeautifulSoup(response.text, 'lxml')    
        result = [elem.text for elem in bs.find_all(class_='da2727fca3 b40b56773d e65bdf6865', limit=12)]
        zodiac_cache["zodiac_list"] = result
        return result
    except requests.exceptions.RequestException as e:
        return [f"Ошибка запроса: {str(e)}"]
    except Exception as e:
        return [f"Ошибка парсинга: {str(e)}"]
	    



		