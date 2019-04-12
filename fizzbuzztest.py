'''
Created on Apr 12, 2019

@author: seamus
'''
import unittest
from fizzbuzz.fizzbuzz import *
import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def testNoConstructor(self):
        fizzbuzzInstance = FizzBuzz()
        self.assertEqual(fizzbuzzInstance.defaultLength, fizzbuzzInstance.length, "Default length not set")


    def testLength(self):
        trialLength = 15
        fizzbuzzInstance = FizzBuzz(trialLength)
        self.assertEqual(fizzbuzzInstance.length, trialLength, "Length not set")
        
    def testIsMultiple(self):
        fizzbuzzInstance = FizzBuzz()
        testCases = [(True, 3, 6), (False, 3, 5), (True, 5, 15), (False, 5, 7)]

        for testType, multiple, integerToCheck in testCases:
            self.multipleofIntTest(testType, multiple, integerToCheck)
        
    def multipleofIntTest(self, testType, multiple, toCheck):
        if testType:
            testFunction = self.assertTrue
            messageForm = "Returned %d is not mutiple of %d"
        else:
            testFunction = self.assertFalse
            messageForm = "Returned %d is mutiple of %d"

        testFunction(FizzBuzz.isMultiple(multiple, toCheck), messageForm  % (multiple, toCheck))

    def testStep(self):
        testCases = [(3, "Fizz"), (5, "Buzz"), (7, "7"), (15, "Fizz Buzz")]
        for stepNumber, expectedResult in testCases:
            result = FizzBuzz.evaluateStep(stepNumber)
            self.assertEqual(result, expectedResult, "Got %s expected %s" % (result, expectedResult))
            
    def testLastStep(self):
        fizzbuzzInstance = FizzBuzz(7)
        self.assertFalse(fizzbuzzInstance.isLastStep(5), "5 is not last step")
        self.assertTrue(fizzbuzzInstance.isLastStep(7), "7 should be last step")
            
    def testRun(self):
        fizzbuzzInstance = FizzBuzz(16)
        expectedString = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz Buzz 16"
        self.assertEqual(expectedString, fizzbuzzInstance.generate(), "Run case failed")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()