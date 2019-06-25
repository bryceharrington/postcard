#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from datetime imp,ort (datetime, timedelta)

import sys, os.path
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from postcard.trello import Trello

class TestTrello(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(1==2)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTrello))
    return suite


if __name__ == '__main__':
    unittest.main()
