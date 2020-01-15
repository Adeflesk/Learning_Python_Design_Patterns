# Singleton is a creational class pattern that lets you ensure
# that a class has onlhy one instance while providing
# global access point to this instance


class Tigger:
    
    def __str__(self):
        return "I'm the only one"
    
    def roar(self):
        return 'Grr!'


a = Tigger()
b = Tigger()
print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Are they the same object? {a is b}')

