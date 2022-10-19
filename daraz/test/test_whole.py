from daraz import scrape
import pandas as pd
search_term = 'nuts'
data_dir = "D:/PycharmProjects/daraz/daraz/data/"


def test_whole():
    scrape.search(search_term)
    assert len(pd.read_csv(data_dir+search_term+'.csv')) == len(pd.read_csv(data_dir+search_term+'_o.csv'))



