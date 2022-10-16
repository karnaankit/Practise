import requests
import json
import pandas as pd

search = 'nuts'


def get_prices(search_title):
    df = pd.DataFrame(columns=['Title', 'Unit', 'Price'])
    search_url = 'https://www.daraz.com.np/catalog/?q=' + search_title
    response = requests.get(search_url)
    response = response.text.split('window.pageData=')[1]
    data = json.loads(response.split('<')[0])
    for item in data['mods']['listItems']:
        title = item['name']
        price = item['price']
        ind = 0
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
        df = df.append({'Title': name, 'Unit': unit, 'Price': price}, ignore_index=True)
    df.to_csv(search_title + '.csv', index=False)


if __name__ == '__main__':
    get_prices(search)
