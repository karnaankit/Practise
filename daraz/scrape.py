import requests
import json
import pandas as pd
import csv
import re
search = 'nuts'
pattern1 = re.compile(r'(\d+)(\s*)(kg|Kg|KG|gm|Gm|G|g)')


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


def get_units(file):
    df = pd.DataFrame(columns=['Title', 'Units', 'Normalized unit', 'Price'])

    def get_name_unit(row1):
        result = list()
        result.append(pattern1.search(row1).group(0))
        result.append(normalize_units(result[0]))
        result.append(re.sub(pattern1, '', row1).strip('-').split('-')[0])
        return result

    def normalize_units(data):
        quantity = re.compile(r'(\d+)')
        uni = re.compile(r'(\d+)(\s*)(gm|Gm|G|g)')
        if re.match(uni, data):
            size = int(quantity.search(data).group(1))/1000
            data = str(size) + 'Kg'
            return data
        else:
            return data
    with open(file) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if row[0] == 'Title':
                continue
            items = get_name_unit(row[0])
            price = row[1]
            df = df.append({'Title': items[2], 'Units': items[0], 'Normalized unit': items[1], 'Price': price}, ignore_index=True)
    df.to_csv('unit.csv', index=False)


if __name__ == '__main__':
    get_prices(search)
    get_units('title.csv')
