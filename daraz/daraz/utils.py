import re
import csv
import pandas as pd
data_dir = "D:/PycharmProjects/daraz/daraz/data/"


def get_name_unit(row1):
    pattern1 = re.compile(r'(?P<amount>\d+)(\s*)(?P<unit>kg|Kg|KG|gm|Gm|G|g)')
    match = re.search(pattern1, row1)
    result = list()
    result.append(str(match.group('amount')) + str(match.group('unit')))
    if str(match.group('unit')).lower() is 'kg':
        result.append(str(int(match.group('amount')) * 1000))
    if str(match.group('unit')).lower() in ['gm', 'g']:
        result.append(str(match.group('amount')))
    result.append('gm')
    result.append(re.sub(pattern1, '', row1).strip('-').split('-')[0])
    return result


def get_units(file, search_term):
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
    df.to_csv(data_dir+search_term+'.csv', index=False)
