import unittest
from test_package import efg


class TestAbc(unittest.TestCase):
    def test_efg(self):
        a = int(2)
        b = int(1)
        self.assertEqual(efg.efg(a, b), 1)