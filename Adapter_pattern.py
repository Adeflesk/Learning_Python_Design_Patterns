#Adapter is a structual design pattern that converts the 
#interface of a class into another interface clients
#expect. Adapter lets classes work together that couldn't otherwise
#because of incompatible interfaces.
from template_method_pattern import FileAverageCalculator
from random import randint

class GeneratorAdapter:

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def readline(self):
        try:
            return next(self.adaptee)
        except StopIteration:
            return ''
    
    def close(self):
        pass

g = (randint(1, 100)for i in range(1000000))
fac = FileAverageCalculator(GeneratorAdapter(g))
print(fac.average())