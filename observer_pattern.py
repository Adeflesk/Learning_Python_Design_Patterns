#Observer is a behavioral desigh pattern
#that defines a one-to-many dependency between
#between objects so that when one object changes state
#all its dependents are notified and update automatically

from abc import ABC, abstractmethod

class Observer(ABC):

     @abstractmethod
     def update(self, observable, *args):
         pass

class Observable:
     def __init__(self):
          self._observers = []

     def add_observer(self, observer):
         self._observers.append(observer)

     def delete_observer(self, observer):
         self._observers.remove(observer)

     def notify_observers(self, *args):
         for observer in self._observers:
             observer.update(self, *args)

class Employee(Observable):

     def __init__(self, name, salary):
          super().__init__()
          self._name = name
          self._salary = salary

     @property
     def name(self):
         return self._name

     @property
     def salary(self):
         return self._salary
      
     @salary.setter
     def salary(self, new_salary):
          self._salary = new_salary
          self.notify_observers(new_salary)

class Payroll(Observer):

     def update(self, change_employee, new_salary):
         print(f'Cut a new check for {change_employee.name}! '
               f'Her/His salary is now {new_salary}!')

class TaxMan(Observer):
     
     def update(self, change_employee, new_salary):
         print(f'Send {change_employee.name} a new tax bill') 


e = Employee('Amy Fowler Fawcett', 5000)
p = Payroll()
t = TaxMan()

e.add_observer(p)
e.add_observer(t)

print('update 1')
e.salary = 6000

e.delete_observer(t)

print('\nUpdate 2')
e.salary = 6500
    

class Twitter(Observable, Observer):

    def __init__(self, name):
        super().__init__()
        self._name = name
        self._tweet = ""

    @property
    def name(self):
        return self._name

   
  
    def follow(self, followed):
        followed.add_observer(self)
        return self
         

    def tweet(self, tweet_message):
        self._tweet = tweet_message
        self.notify_observers(tweet_message)

    
    def update(self, followed, tweet_message):
        print(f'{self.name} recieved a tweet from '
              f'{followed.name} '
              f':{tweet_message}')

a = Twitter('Alice')
k = Twitter('King')
q = Twitter('Queen')
h = Twitter('Mad Hatter')
c = Twitter('Cheshire Cat')
a.follow(c).follow(h).follow(q) 
k.follow(q)
q.follow(q).follow(h)
h.follow(a).follow(q).follow(c)


print(f'==== {q.name} tweets ====')
q.tweet('Off with their heads!')
print(f'\n==== {a.name} tweets ====')
a.tweet('What a strange world we live in.')
print(f'\n==== {k.name} tweets ====')
k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
print(f'\n==== {c.name} tweets ====')
c.tweet("We're all mad here.")
print(f'\n==== {h.name} tweets ====')
h.tweet('Why is a raven like a writing-desk?')