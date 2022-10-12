from test_package import abc


def test_abc():
    a = int(1)
    b = int(2)
    assert abc.abc(a, b) == 3
