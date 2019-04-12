'''
Created on Apr 12, 2019

@author: seamus
'''
import unittest
from fizzbuzz.fizzbuzz import *


class TestFizzBuzz(unittest.TestCase):

    def testNoConstructor(self):
        fizzbuzzInstance = FizzBuzz()
        self.assertEqual(fizzbuzzInstance.defaultLength, fizzbuzzInstance.length, "Default length not set")


    def testLength(self):
        trialLength = 15
        fizzbuzzInstance = FizzBuzz(trialLength)
        self.assertEqual(fizzbuzzInstance.length, trialLength, "Length not set")
        
    def testIsMultipleThree(self):
        fizzbuzzInstance = FizzBuzz()
        self.assertTrue(FizzBuzz.isMultipleThree(3))
        self.assertFalse(FizzBuzz.isMultipleThree(5))

    def testIsMultipleFive(self):
        fizzbuzzInstance = FizzBuzz()
        self.assertFalse(FizzBuzz.isMultipleFive(3))
        self.assertTrue(FizzBuzz.isMultipleFive(5))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()