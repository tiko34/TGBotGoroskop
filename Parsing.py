## -*- coding: utf-8 -*-
import requests # type: ignore
#Библиотека для парсинга
from bs4 import BeautifulSoup # type: ignore


global url
url='https://horo.mail.ru/prediction/'

def parsing_site(zodiac,day):
		correct_url=url+zodiac+'/'+day+'/'
		response = requests.get(correct_url)
		bs = BeautifulSoup(response.text,'lxml')
		result = bs.findAll('p')
		return result