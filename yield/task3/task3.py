''''''
'''
Генератор принимает список ссылок Скачивает по очереди и елдит(yield)

.__dict__.keys() - чтобы все функции увидеть 

print(response) # <Response [200]> - [200] это код ответа Http протокла
'''
import requests
def download_list(l):
    for site in l:
        yield requests.get(site).text

r = download_list(["https://jsonplaceholder.typicode.com/users", "http://www.paulbrownmagic.com/blog/generator_send.html"])
print(next(r))
print(next(r))