import requests
from bs4 import BeautifulSoup

response = requests.get('https://bitcoin.org/ru/')
html_text = response.text

soup = BeautifulSoup(response.text, 'lxml')

urls, images = [], []

for link in soup.find_all("a"):
    urls.append(link.get('href'))

for link in soup.find_all("img"):
    images.append(f"https://bitcoin.org{link.get('src')}")

new_list_with_urls = []

for url in urls:
    if url is None:
        continue
    else:
        if url.startswith('/'):
            new_list_with_urls.append(f"https://bitcoin.org{url}")
        else:
            new_list_with_urls.append(f"https://bitcoin.org/{url}")

print(images)
print(new_list_with_urls)
