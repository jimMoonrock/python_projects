import requests
from bs4 import BeautifulSoup

s = requests.session()
data = {'login': 'richardpy90@gmail.com', 'password': 'fuckthishit123890'}
url = 'https://proglib.io/#'
r = s.post(url, data=data)
response = requests.get(url)
#html_text = response.text
soup = BeautifulSoup(response.text, 'lxml')

lol = soup.find('body').find_all('article', class_='block preview-card  ')
print(lol)
