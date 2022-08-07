from bs4 import BeautifulSoup as Bs
import requests
import pandas as pd
from tkinter import *

#Listas e dicionário
#listas e o dicionario não precisam ser retornados porque estão globais
products_dic = {}
list_names_prices = []
list_names = []
list_prices = []
list_discounts = []

#Entrada
name = str(input('Nome do produto: '))

#Link e numero de paginas
def link_numpg(name):
    link = f'https://lista.mercadolivre.com.br/{name}#D[A:{name}]'
    num_pages = int(str(Bs((requests.get(link)).content,
    'html.parser').find('li',
    {'class': 'andes-pagination__page-count'}).text)[3:])
    return [link, num_pages]

#entrada do item de pesquisa e retornando o link e numeros de paginas em uma lista
link_numpages = link_numpg(name)
link = link_numpages[0]
num_pages = link_numpages[1]

#Varredura dos produtos
def products_sweep(link, num_pages):
    page_actual = num_pages 
    while True:
        print(f'Paginas restantes = {num_pages}\n'
        f'Pagina atual = {page_actual - num_pages}')
        request = requests.get(link)
        bs = Bs(request.content, 'html.parser')
        products = bs.find_all('li',
        {'class': 'ui-search-layout__item'})
        for product in products:
            name = product.find('h2',
            {'class': 'ui-search-item__title'}).text
            price = product.find('span',
            {'class': 'price-tag-amount'}).text
            try:
                discount = str(product.find('span',
                {'class': 'ui-search-price__discount'}).text).replace('OFF', '')
            except:
                discount = '0%'
            print(discount)
            list_names.append(name)
            list_prices.append(price)
            list_discounts.append(discount)
        try:
            link = bs.find('a', {'class':
            'andes-pagination__link ui-search-link',
            'title': 'Seguinte'})['href']
        except:
            #Paginas acabaram
            break
        num_pages -= 1


#entrada do link e num_pages e preenchendo as listas e o dicionario
products_sweep(link, num_pages)

#DataFrame e Excel
products_dic['Nome'] = list_names
products_dic['Preço'] = list_prices
products_dic['Desconto'] = list_discounts
del list_names, list_prices, list_discounts
products_df = pd.DataFrame(products_dic)
products_df.to_excel('project13/products_df.xlsx')
