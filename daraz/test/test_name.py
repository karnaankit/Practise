from daraz import scrape
title = 'True Elements Berries Mix 30g - Mix of Cranberries & Blueberries Healthy Snack Berry Mix Dried Berries'
items = ['30g', '0.03Kg', 'True Elements Berries Mix  ']


def test_name():
    item = scrape.get_name_unit(title)
    assert item == items



