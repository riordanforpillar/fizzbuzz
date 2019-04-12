'''
Created on Apr 12, 2019

@author: seamus
'''

class FizzBuzz(object):
    '''
    classdocs
    '''
    
    defaultLength = 15

    def __init__(self, length = defaultLength):
        '''
        Constructor
        '''
        self.length = length
        
        
    def isMultipleThree(integerToCheck):
        if integerToCheck % 3 == 0:
            return True
        return False

    def isMultipleFive(integerToCheck):
        if integerToCheck % 5 == 0:
            return True
        return False        