'''
Created on Apr 12, 2019

@author: seamus
'''
import unittest
from fizzbuzz.fizzbuzz import *


class TestFizzBuzz(unittest.TestCase):


    def testFizzBuzzLength(self):
        trialLength = 15
        fizzbuzzInstance = FizzBuzz(trialLength)
        self.assertEqual(fizzbuzzInstance.length, trialLength, "Length not set")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()