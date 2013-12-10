#!/usr/bin/env python

import unittest
from datetime import datetime
from LunchEvent import LunchEvent

class TestLunhEvent(unittest.TestCase):
    def setUp(self):
        self.event = LunchEvent("pizza", "2013-12-09")

    def test_date_conversion(self):
        expected_date = datetime(2013, 12, 9)
        self.assertEqual(self.event.date, expected_date)


if __name__ == '__main__':
    unittest.main()

