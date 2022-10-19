import re
import csv
import pandas as pd
data_dir = "D:/PycharmProjects/daraz/daraz/data/"


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
