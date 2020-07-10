import requests
from bs4 import BeautifulSoup
import csv
import sys
import webbrowser
#inp = input("Enter the text you want to search: ")
URL = "https://indianexpress.com/section/cities/chennai/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
link = soup.find_all('h6')
data = {}
cnt = 1
for i in link:
    i1 = i.find('a').text.strip()
    data[cnt] = [i1]
    data[cnt].append(i.find('a').get('href'))
    cnt+=1
for i,j  in data.items():
    print(str(i)+": "+j[0])
    print()
res = True
while(res):
    choice = input("Enter The Choice or 'e' to end the reading: ")
    if choice == 'e':
        res = False
        print("reading ended")
    elif choice.isdigit() and int(choice)<=len(data):
        print(data[int(choice)][1])
        webbrowser.open_new_tab(data[int(choice)][1]) 

    else:print("choice you have entered is wrong")
sys.exit()
