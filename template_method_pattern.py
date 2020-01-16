#Template method is a behavioral design
# pattern that defines the skeleton of an algorithm
# in the base class but lets derived classes overide specific
# steps of the algorithm without changing its structure

from abc import ABC, abstractmethod
#The AverageCalculator class is an abstract base class
class AverageCalculator(ABC):

    def average(self):
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()


    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next_item(self):
        pass

    
    def dispose(self):
        pass

class FileAverageCalculator(AverageCalculator):

    def __init__(self, file):
        self.file = file
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ''

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline()
        return result
    
    def dispose(self):
        self.file.close()

fac = FileAverageCalculator(open('data.txt'))
print(fac.average())#call the template method