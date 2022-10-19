import requests
import json
import pandas as pd
import csv
import os
import utils
data_dir = "D:/PycharmProjects/daraz/daraz/data/"


def search(search_term):

    def get_prices(search_title):
        df = pd.DataFrame(columns=['Title', 'Price'])
        search_url = 'https://www.daraz.com.np/catalog/?q=' + search_title
        response = requests.get(search_url)
        response = response.text.split('window.pageData=')[1]
        data = json.loads(response.split('</script>')[0])
        for item in data['mods']['listItems']:
            title = item['name']
            price = item['price']
            df = df.append({'Title': title, 'Price': price}, ignore_index=True)
        df.to_csv(data_dir+search_title+'_o.csv', index=False)
    if search_term + '.csv' in os.listdir(data_dir):
        view_data(search_term)
    else:
        get_prices(search_term)
        process(search_term)


def process(search_term):
    utils.get_units(data_dir + search_term + '_o.csv', search_term)
    view_data(search_term)


def view_data(item):
    df1 = pd.DataFrame(columns=['Title', 'Units', 'Amount', 'Normalized unit', 'Price'])
    with open(data_dir + item + '.csv') as f:
        csvreader1 = csv.reader(f)
        for row in csvreader1:
            if row[0] == 'Title':
                continue
            df1 = df1.append({'Title': row[0], 'Units': row[1], 'Amount': row[2], 'Normalized unit': row[3],
                              'Price': row[4]}, ignore_index=True)
        print(df1)
