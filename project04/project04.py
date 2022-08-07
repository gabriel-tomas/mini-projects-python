import requests
from bs4 import BeautifulSoup as bs
from tkinter import *


dict_items = {}
list_price = []
list_name = []
product = str(input("Item: "))
site = f"https://lista.mercadolivre.com.br/{product}#D[A:{product}]"
bs_num_pages = bs(requests.get(site).content, 'html.parser')
site_num_pages = int(str(bs_num_pages.find('li',
{'class': 'andes-pagination__page-count'}).text)[3:])
print(f'Pages: {site_num_pages}')
num_page = 0
while True:
    try:
        while True:
            site_page = requests.get(site)
            status_page = site_page.status_code
            print(status_page)
            if status_page == 200:
                break
        bs4 = bs(site_page.content, 'html.parser')
        site = bs4.find('a', {'class':
        'andes-pagination__link ui-search-link',
        'title': 'Seguinte'})['href']
        print(site)
        items = bs4.find_all('li', {'class': 'ui-search-layout__item'})
        for item in items:
            name = item.find('h2', {'class': 'ui-search-item__title'}).text
            price = str(item.find('span', {'class':'price-tag ui-search-price__part'}).text)
            price = float(str(item.find('span',{'class':'price-tag ui-search-price__part'}
            ).text).replace('.', '').replace(',', '.')[price.index('R$') + 2:])
            list_name.append(name)
            list_price.append(price)
        dict_items[f'item {num_page}'] = list_item[:]
        num_page += 1
        site_num_pages -= 1
        print(f"page: {num_page}")
        print(f"remaining: {site_num_pages}")
    
    except:
        print('Pages finished')
        break
    if num_page == 1:
        break
print(len(list_name), len(list_price))

while True:
    item_search_bigger = float(input('bigger then: '))
    item_search_less = float(input('Less than: '))
    for items in dict_items.values():
        for item in items:
            if item_search_less <= item[1] <= item_search_bigger:
                print(item)
