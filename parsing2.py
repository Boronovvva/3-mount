from bs4 import BeautifulSoup
import requests

number_news = 0
for page in range(1, 100):
    url = f'https://stopgame.ru/news/all/p1{page}/'
    response = requests.get(url= url)
    # print(response)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)
    all_news = soup.find_all('a', class_ = '_title_11mk8_60')
    # print(all_news)
    for news in all_news:
        number_news +=1
        print (f"{number_news}) {news.text}")