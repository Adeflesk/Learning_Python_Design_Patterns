#Chained comparison operators
x = 7
if 0 < x < 10:
    print('x is greater than 0 but less than 10')

my_collection =  [10,20,33,14,16,33,44]

def answer_number(number):
    return 10 if number < 5 else 20

print(answer_number(x))
#proper way to iterate over a collection
for index, value in enumerate(my_collection):
    print(index, value)