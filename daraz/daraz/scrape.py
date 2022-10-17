import requests
import json
import pandas as pd
import csv
import re
import os


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
        df.to_csv('title.csv', index=False)

    def get_name_unit(row1):
        amount = re.compile(r'(\d+)')
        pattern1 = re.compile(r'(\d+)(\s*)(kg|Kg|KG|gm|Gm|G|g)')
        result = list()
        result.append(pattern1.search(row1).group(0))
        temp = normalize_units(result[0])
        if re.match(amount, temp):
            result.append(amount.search(temp).group(1))
            result.append(re.sub(amount, '', temp))
        result.append(re.sub(pattern1, '', row1).strip('-').split('-')[0])
        return result

    def normalize_units(data):
        quantity = re.compile(r'(\d+)')
        uni = re.compile(r'(\d+)(\s*)(kg|Kg|KG|kG)')
        data = re.sub(r'(\s*)(gm|Gm|G|g)', 'gm', data)
        if re.match(uni, data):
            size = int(quantity.search(data).group(1)) * 1000
            data = str(size) + 'gm'
            return data
        else:
            return data

    def get_units(file):
        df = pd.DataFrame(columns=['Title', 'Units', 'Amount', 'Normalized unit', 'Price'])
        with open(file) as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                if row[0] == 'Title':
                    continue
                items = get_name_unit(row[0])
                price = row[1]
                df = df.append({'Title': items[3], 'Units': items[0], 'Amount': items[1], 'Normalized unit': items[2],
                                'Price': price}, ignore_index=True)
        df.to_csv(os.getcwd()+'/data/'+search_term+'.csv', index=False)

    def view_data(item):
        df1 = pd.DataFrame(columns=['Title', 'Units', 'Amount', 'Normalized unit', 'Price'])
        with open(path + '/' + item + '.csv') as f:
            csvreader1 = csv.reader(f)
            for row in csvreader1:
                if row[0] == 'Title':
                    continue
                df1 = df1.append({'Title': row[0], 'Units': row[1], 'Amount': row[2], 'Normalized unit': row[3],
                                  'Price': row[4]}, ignore_index=True)
            print(df1)
    path = os.getcwd() + '/data'
    if search_term + '.csv' in os.listdir(path):
        view_data(search_term)
    else:
        get_prices(search_term)
        get_units('title.csv')
        os.remove('title.csv')
        view_data(search_term)


if __name__ == '__main__':
    search('nuts')
