#!/usr/bin/env python

import unittest
from LuncherPreferences import LuncherPreferences

class TestLuncherPreferences(unittest.TestCase):
    def setUp(self):
        self.luncherprefs = LuncherPreferences("ryan")

    def test_add_over_100(self):
        self.luncherprefs.update("pizza", 50)
        self.luncherprefs.update("cafe", 60)
        self.luncherprefs.normalize()

        self.assertEqual(sum(self.luncherprefs.preferences.values()), 100)
        self.assertEqual(round(self.luncherprefs.preferences["pizza"]), 45)
        self.assertEqual(round(self.luncherprefs.preferences["cafe"]), 55)


if __name__ == '__main__':
    unittest.main()

