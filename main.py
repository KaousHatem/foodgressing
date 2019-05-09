from requests import Session
from bs4 import BeautifulSoup
import pandas as pd 
import io,os


session = Session()
headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
		}

MAIN_URL = "https://foodgressing.com/mcdonalds-menu-prices-canada/?fbclid=IwAR1qJuufIbo6lrrE-xqSzA7ycEzY4CeGLiL6txTaXmE0xehxMxD_HD2U10E"


with session.request(method='GET',url=MAIN_URL,headers=headers) as response:
	soup = BeautifulSoup(response.text,'html.parser')
	# print(soup.find("table").find('thead'))
	header = [item.text for item in soup.find("table").find('thead').findAll('th')]
	print(header)
	rows = [ [i.text for i in item.findAll('td')] for item in soup.find("table").find('tbody').findAll('tr') ]
	df = pd.DataFrame(rows,columns=header)
	df.to_csv("table.csv")