## -*- coding: utf-8 -*-
import requests # type: ignore
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
		result+=parsing_site_date(day)
		result += bs.findAll('p')
		for temp in result:
			if result == '<p>{"captchaPath":"/captcha/img/6","isRlimitedAgain":false}</p>':
				return '0' 
			else: 
				return result
	except :
	    return '0'



			

def parsing_site_date(day):
	try:
		correct_url=url+'taurus'+'/'+day+'/'
		response = requests.get(correct_url)
		bs = BeautifulSoup(response.text,'lxml')
		result = bs.find('span', class_='f2eee589ba de333e7f31 e1df578fc6 e53e657292 a7a6fb85f2')
		return result
	except :
	    return '0'


		