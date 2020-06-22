"""
Program: test_functions.py
Author: Sherri Maya
Last date modified: 06/21/2020



Test camper_age_input.py
"""

import unittest

from main import camper_age_input as camp

class FunctionTestCase(unittest.TestCase):

    def test_convert_to_months(self):
        self.assertEqual(camp.convert_to_months(12), 144)

if __name__ == '__main__':
    unittest.main()
