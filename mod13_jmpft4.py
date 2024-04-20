import unittest
from datetime import datetime

def testSymbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def testChartType(chart):
    return chart in ['1','2']

def testTimeSeries(series):
    return series in ['1','2','3','4']

def testStartDate(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def testEndDate(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class TestCases(unittest.TestCase):
    def testSymbol(self):
        self.assertTrue(testSymbol("AAPL"))
        self.assertTrue(testSymbol("SPY"))
        self.assertFalse(testSymbol("tech"))
        self.assertFalse(testSymbol("fake"))

    def testChartType(self):
        self.assertTrue(testChartType("1"))
        self.assertTrue(testChartType("2"))
        self.assertFalse(testChartType("3"))
        self.assertFalse(testChartType("A"))

    def testTimeSeries(self):
        self.assertTrue(testTimeSeries("1"))
        self.assertTrue(testTimeSeries("4"))
        self.assertFalse(testTimeSeries("5"))
        self.assertFalse(testTimeSeries("A"))

    def testStartDate(self):
        self.assertTrue(testStartDate("2024-01-01"))
        self.assertFalse(testStartDate("2024/01/01"))
        self.assertFalse(testStartDate("24-01-01"))

    def testEndDate(self):
        self.assertTrue(testEndDate("2024-12-31"))
        self.assertFalse(testEndDate("2024/12/31"))
        self.assertFalse(testEndDate("24-12-31"))    

if __name__ == '__main__':
    unittest.main()
