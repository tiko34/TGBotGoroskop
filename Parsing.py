## -*- coding: utf-8 -*-
import requests # type: ignore
#Эмодзи 
from Emoji import EmojiError
#Библиотека для парсинга
from bs4 import BeautifulSoup # type: ignore

global url
url='https://horo.mail.ru/prediction/'

async def parsing_site(zodiac,day):
	try:
		correct_url=url+zodiac+'/'+day+'/'
		response = requests.get(correct_url)
		bs = BeautifulSoup(response.text,'lxml')
		result=[]
		result += bs.find('span', class_='f2eee589ba cd39273477 e1df578fc6 e53e657292 a7a6fb85f2')
		result += bs.findAll('p')
		return await result
	except Exception:
		return  await EmojiError
		
	    



		