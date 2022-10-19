from daraz import scrape
import pandas as pd
from daraz import utils
import os
search_term = 'rice'
data_dir = "D:/PycharmProjects/daraz/daraz/data/"


def test_scrape():
    os.remove(data_dir + search_term + '_o.csv')
    os.remove(data_dir + search_term + '.csv')
    scrape.search(search_term)
    assert len(pd.read_csv(data_dir+search_term+'.csv')) == len(pd.read_csv(data_dir+search_term+'_o.csv'))


def test_process():
    os.remove(data_dir + search_term + '.csv')
    scrape.process(search_term)
    assert len(pd.read_csv(data_dir+search_term+'.csv')) == len(pd.read_csv(data_dir+search_term+'_o.csv'))
    assert len(pd.read_csv(data_dir+search_term+'.csv')) and len(pd.read_csv(data_dir+search_term+'_o.csv')) > 1

def test_get_name_unit():
    assert utils.get_name_unit('Peanuts 1kg') == ['1kg', '1000', 'gm', 'Peanuts ']
    assert utils.get_name_unit('Almond Nuts 500g') == ['500g', '500', 'gm', 'Almond Nuts ']
    assert utils.get_name_unit('Bhumi Nepal Dried Cranberry-500 g') == ['500g', '500', 'gm', 'Bhumi Nepal Dried Cranberry']
    assert utils.get_name_unit('Soft Walnut / Okhar - 200Gm') == ['200Gm', '200', 'gm', 'Soft Walnut / Okhar ']
