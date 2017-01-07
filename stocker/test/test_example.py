# -*- coding: utf-8 -*-
"""
:author: Harold Dennis C Batocael
:contact: hardistones@gmail.com
"""
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, 1 + 1)


if __name__ == '__main__':
    unittest.main()
