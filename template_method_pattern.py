#Template method is a behavioral design
# pattern that defines the skeleton of an algorithm
# in the base class but lets derived classes overide specific
# steps of the algorithm without changing its structure

from abc import abstractmethod

class AverageCalculator(ABC):

    def average(self):
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError('Can't compute average of zero items."")
            return total_sum / num_items
            finally:
                self.dispose()


    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next_item(self):
        pass

    @abstractmethod
    def dispose(self):
        pass