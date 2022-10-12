import unittest
from test_package import ret


class TestRet(unittest.TestCase):
    def test_ret(self):
        data = 1
        result = ret.test(data)
        self.assertEqual(result, data)


if __name__ == '__main__':
    unittest.main()
