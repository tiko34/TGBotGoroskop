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
		result += bs.find('span', class_='f2eee589ba c6eb8d9a4c')
		result += bs.find('span', class_='f2eee589ba cd39273477 e1df578fc6 e53e657292 a7a6fb85f2')
		result += bs.findAll('p')
		return result
	except Exception:
		return  error

def parsing_site_zodiac_List():
	url_zodiac_list="https://horo.mail.ru/prediction/tomorrow/"
	response = requests.get(url_zodiac_list)
	bs = BeautifulSoup(response.text,'lxml')
	result=[]
	for elem in bs.find_all(class_='da2727fca3 b40b56773d e65bdf6865'):
		result.append(elem.text)
	return result
	    



		