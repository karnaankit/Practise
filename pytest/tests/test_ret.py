from test_package import ret


def test_ret():
    data = [1, 2, 3]
    for num in data:
        assert ret.test(num) == num
