## -*- coding: utf-8 -*-
import requests # type: ignore
#Эмодзи 
from Emoji import error
#Библиотека для парсинга
from bs4 import BeautifulSoup # type: ignore

global url
url='https://horo.mail.ru/prediction/'

def parsing_site(zodiac,day):
	try:
		correct_url=url+zodiac+'/'+day+'/'
		response = requests.get(correct_url)
		bs = BeautifulSoup(response.text,'lxml')
		result=[]
# Парсим из страницы дату 
		result += bs.find('span', class_='f2eee589ba de333e7f31 e1df578fc6 e53e657292 a7a6fb85f2')
# Парсим из страницу текст гороскопа
		result += bs.findAll('p')
		return result
	except Exception:
	    return  error



		