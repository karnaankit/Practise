import unittest
from test_package import abc


class TestAbc(unittest.TestCase):
    def test_abc(self):
        a = int(1)
        b = int(2)
        self.assertEqual(abc.abc(a, b), 3)
