import requests

from bs4 import BeautifulSoup
import pandas as pd

#page=requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997#.XmLBKlRR3IU')

page = requests.get('https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

#page = requests.get('https://www.amazon.in/gp/cart/view.html?ref_=nav_cart')

soup=BeautifulSoup(page.content, 'html.parser')


#container= soup.find_all('div', class_ ='a-row sc-list-item sc-list-item-border sc-java-remote-feature')


container= soup.find_all('div', class_ ='_3liAhj')
titles=[item.find(class_='_2cLu-l').get_text() for item in container]

price=[item.find(class_='_1vC4OE').get_text() for item in container]

ratings=[item.find(class_='hGSR34').get_text() for item in container]

"""dis_item=soup.find(class_='VGWI6T')
dis_item.span.clear()
discount=[item.get_text() for item in dis_item]
"""
#print(titles)
#print(soup.prettify(container[0]))
#print(container[0])
#week =soup.find(id='seven-day-forecast-body')

table=pd.DataFrame({'Phone Names':titles, 'Price' : price, 'Ratings' :ratings})
print(table)

table.to_csv(r'C:\Users\Vaio\Desktop\iPhones.csv')

#print(week.find_all(class_='list-unstyled'))