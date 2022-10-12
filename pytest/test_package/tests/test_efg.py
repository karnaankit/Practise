from test_package import efg


def test_efg():
    a = int(2)
    b = int(1)
    assert efg.efg(a, b) == 1