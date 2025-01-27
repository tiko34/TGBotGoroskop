## -*- coding: utf-8 -*-
import requests # type: ignore
#Библиотека для парсинга
from bs4 import BeautifulSoup # type: ignore

global url
url='https://horo.mail.ru/prediction/'

session = requests.Session()

# Ускоренный парсинг для получения данных
def parsing_site(zodiac, day):
    try:
        correct_url = f"{url}{zodiac}/{day}/"
        response = session.get(correct_url, timeout=5)
        response.raise_for_status()
        bs = BeautifulSoup(response.text, 'lxml')
        result = []  
        # Используем find_all с ограничением на количество элементов для повышения скорости
        result += bs.find_all('span', class_='f2eee589ba c6eb8d9a4c', limit=1)
        result += bs.find_all('span', class_='f2eee589ba cd39273477 e1df578fc6 e53e657292 a7a6fb85f2', limit=1)
        result += bs.find_all('p', limit=5)
        return result
    except requests.exceptions.RequestException as e:
        return [f"Ошибка запроса: {str(e)}"]
    except Exception as e:
        return [f"Ошибка парсинга: {str(e)}"]

#Для кеширования списка знаков зодиака
zodiac_cache = {}
def parsing_site_zodiac_List():
    if "zodiac_list" in zodiac_cache:
        return zodiac_cache["zodiac_list"]
    
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
	    



		