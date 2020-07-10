#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "https://www.livechennai.com/gold_silverrate.asp"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser') 

quotes=[] # a list to store quotes 

gold = soup.find('table', attrs='table-price')
for row in gold.findAll('td', attrs='content'):
    row = row.find('font',attrs='txt-clr')
    quotes.append(row.text.strip())
day1 = quotes[0:5]
day2 = quotes[5:10]
dif = float(day1[1])-float(day2[1])

if dif <0:print("Gold Rate is 'decreased' by {} finally the rate is {}".format(abs(dif),day1[1]))
elif dif >0:print("Gold Rate is 'increased' by {} finally the rate is {}".format(abs(dif),day1[1]))
else:print("rate is ideal")
