from daraz import scrape
import pandas as pd
from daraz import utils
search_term = 'nuts'
data_dir = "D:/PycharmProjects/daraz/daraz/data/"


def test_scrape():
    scrape.search(search_term)
    assert len(pd.read_csv(data_dir+search_term+'.csv')) == len(pd.read_csv(data_dir+search_term+'_o.csv'))


def test_process():
    scrape.process(search_term)
    assert len(pd.read_python_csv(data_dir+search_term+'.csv')) == len(pd.read_csv(data_dir+search_term+'_o.csv'))


def test_get_name_unit():
    test_data = 'Peanuts 1kg'
    assert utils.get_name_unit(test_data) == ['1kg', '1000', 'gm', 'Peanuts ']
