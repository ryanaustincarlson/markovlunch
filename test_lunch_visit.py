#!/usr/bin/env python

import unittest
from datetime import datetime, timedelta
from LunchVisit import LunchVisit

class TestLunchVisit(unittest.TestCase):

    def test_date_conversion(self):
        visit = LunchVisit("pizza", "2013-12-09")
        expected_date = datetime(2013, 12, 9)
        self.assertEqual(visit.date, expected_date)

    def set_up_visit(self, days_behind):
        visit = LunchVisit("pizza", "2013-12-09")
        visit.date = datetime.now() - timedelta(days=days_behind)
        visit.compute_discount()
        return visit

    def test_discounts_recent(self):
        visit = self.set_up_visit(1)
        self.assertEqual(visit.discount, 0)

    def test_discounts_1week(self):
        visit = self.set_up_visit(9)
        self.assertEqual(visit.discount, 1/3.)

    def test_discounts_2week(self):
        visit = self.set_up_visit(15)
        self.assertEqual(visit.discount, 2/3.)
        
    def test_discounts_later(self):
        visit = self.set_up_visit(100)
        self.assertEqual(visit.discount, 1)


if __name__ == '__main__':
    unittest.main()

