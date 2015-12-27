'''
Created on 27.12.2015

@author: marcelkisilowski
'''
import unittest
from Finance.yahoo_api import yahoo_api
from datetime import date
import Finance.dateUtils as du 
class YahooAPITests(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        self.api = yahoo_api()
        
    def test_getDate(self):
        self.assertEqual(du.to_date("22.01.2010"), date(2010,01,22), "Wrong Date")
    def test_MonthsDiff(self):
        self.assertEqual(du.checkMonthsBetweenDates(date(2010,02,21), date(2011,02,21)), 12, "Wrong diff")
        self.assertEqual(du.checkMonthsBetweenDates(date(2010,02,21), date(2012,02,22)), 24, "Wrong diff")
        self.assertEqual(du.checkMonthsBetweenDates(date(2010,02,21), date(2010,10,22)), 8, "Wrong diff")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(YahooAPITests)
    unittest.TextTestRunner(verbosity=4).run(suite)