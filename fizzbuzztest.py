'''
Created on Apr 12, 2019

@author: seamus
'''
import unittest
import fizzbuzz.fizzbuzz as fb


class TestFizzBuzz(unittest.TestCase):

    def testNoConstructor(self):
        fizzbuzzInstance = fb.FizzBuzz()
        self.assertEqual(fizzbuzzInstance.defaultLength, fizzbuzzInstance.length, "Default length not set")


    def testLength(self):
        trialLength = 15
        fizzbuzzInstance = fb.FizzBuzz(trialLength)
        self.assertEqual(fizzbuzzInstance.length, trialLength, "Length not set")
        
    def testIsMultiple(self):
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

        testFunction(fb.FizzBuzz.isMultiple(multiple, toCheck), messageForm  % (multiple, toCheck))

    def testStep(self):
        testCases = [(3, "fizz"), (5, "buzz"), (7, "7"), (15, "fizzbuzz"), (30, "fizzbuzz")]
            
        for stepNumber, expectedResult in testCases:
            result = fb.FizzBuzz.evaluateStep(stepNumber)
            self.assertEqual(result, expectedResult, "Got %s expected %s" % (result, expectedResult))
            
    def testLastStep(self):
        fizzbuzzInstance = fb.FizzBuzz(7)
        self.assertFalse(fizzbuzzInstance.isLastStep(5), "5 is not last step")
        self.assertTrue(fizzbuzzInstance.isLastStep(7), "7 should be last step")
            
    def testRun(self):
        fizzbuzzInstance = fb.FizzBuzz(16)
        expectedString = "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16"
        self.assertEqual(expectedString, fizzbuzzInstance.generate(), "Run case failed")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()