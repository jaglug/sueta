News=[]
Fnews=[]
from bs4 import BeautifulSoup
import requests
url='https://habr.com/ru/hub/infosecurity'
page = requests.get(url) 
soup=BeautifulSoup(page.text, "html.parser")
News=soup.find_all('a', class_='tm-article-snippet__title-link')
link=soup.find_all('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2')

for data in News:
    if data.find('span') is not None:
        Fnews.append(data.text)
with open ('C:/Users/Admin/Desktop/parser.txt','w') as f:
    for data in Fnews:
        print(data,file=f)
    for name in link:
        print(name.a['href'],file=f)
#программа парсит названия статей и ссылки на них