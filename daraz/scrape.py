import requests
from selenium import webdriver
import json
import time
import pandas as pd
from bs4 import BeautifulSoup
DRIVER_PATH = 'D:/PycharmProjects/daraz/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
search_title = 'nuts'
search_url = 'https://www.daraz.com.np/catalog/?q=' + search_title
driver.get(search_url)
time.sleep(5)
response = driver.page_source
driver.quit()
search_soup = BeautifulSoup(response, 'html.parser')
results = search_soup.find_all('div', {'class': 'gridItem--Yd0sa'})
df = pd.DataFrame(columns=['Title', 'Unit', 'Price'])
for result in results:
    ind = 0
    title = result.find('a', {'title': True}).get('title')
    for char in title:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            name = title[:ind]
            unit = title[ind:]
            for char1 in unit:
                if char1 in ['g', 'G']:
                    unit = unit[:unit.index(char1) + 1]
                    break
            break
        ind += 1
    price = result.find('span', {'class': 'currency--GVKjl'}).text
    df.loc[len(df)] = [name, unit, price]
df.to_csv(search_title + '.csv', index=False)
