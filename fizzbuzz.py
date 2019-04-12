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
        
    def run(self):
        print(self.generate())
        
    def generate(self):
        evalutedString = ""
        for i in range(1,self.length+1):
            evalutedString += FizzBuzz.evaluateStep(i)
            if not self.isLastStep(i):
                evalutedString += " "
        return evalutedString
    
    def isLastStep(self, step):
        if step == self.length:
            return True
        return False
        
    def evaluateStep(step):
        isMultThree = FizzBuzz.isMultiple(3, step)
        isMultFive  = FizzBuzz.isMultiple(5, step)
        
        if isMultThree and isMultFive:
            return "fizzbuzz"
        if isMultThree:
            return "fizz"
        if isMultFive:
            return "buzz"
        return str(step)
    
    def isMultiple(multiple, integerToCheck):
        if integerToCheck % multiple == 0:
            return True
        return False
        
if __name__ == '__main__':
    fizzbuzz = FizzBuzz(18)
    fizzbuzz.run()
    
    
    
    