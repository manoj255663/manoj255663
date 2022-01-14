from bs4 import BeautifulSoup
import requests
import csv

file = open('Zomato.csv','a',encoding='utf-8')
fieldnames = ['name','price','rating','count_rating','count_review']
number_of_page=4
re=requests.get('https://www.zomato.com/indore/order-food-online?utm_source=Google&utm_medium=CPC&utm_term=zomato&utm_campaign=Gsearch_P-Web_O-NA_C-Brand_A-NewUser_SC-Generic_L-Indore_AllEvents&gclid=Cj0KCQjwjMfoBRDDARIsAMUjNZqJQV86ndFupCz2PKoq5d3qHKU0Wr93mzXTpHyUXJjfLnbb4XsugOoaAmbVEALw_wcB')
soup = BeautifulSoup(re.content,'html.parser')
item_list=[]
content = soup.find_all('div',class_='bhgxx2 col-12-12')

for item in content:
    item_name = item.find('div',class_='_3wU53n')
    item_price = item.find('div',class_='_1vC4OE _2rQ-NK')
    item_rating = item.find('div',class_='hGSR34')
    rating_reviews = item.find('span',class_='_38sUEc')

    if item_name is not None:

        textlist = rating_reviews.text.split()

        item_dic = {'name':item_name.text,
                    'price':item_price.text,
                    'rating':item_rating.text,
                    'count_rating':textlist[0],
                    'count_reviews':textlist[3]}
        item_list.append(item_dic)
        print(item_dic)
