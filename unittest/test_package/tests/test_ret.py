import unittest
from test_package import ret


class TestRet(unittest.TestCase):
    def test_ret(self):
        data = [1,2,3]
        for num in data:
            self.assertEqual(ret.test(num), num)
