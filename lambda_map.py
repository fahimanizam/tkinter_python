x = lambda a: a + 10
print(x(5))  # 15

x = lambda a, b: a * b
print("a * b = ", x(5, 6))  # 30

x = lambda a, b, c: a + b + c
print("a + b + c = ", x(5, 6, 2))

lambda_cube = lambda y: y * y * y
print("Cube = ", lambda_cube(5))

# get odd number
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print("Odd numbers = ", final_list)

nums1 = [2, 3, 5, 6, 76, 4, 3, 2]
bads = list(filter(lambda x: x > 4, nums1))
print("number less than 4 = ", bads)

# Get square
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

ani = ['dog', 'cat', 'parrot', 'rabbit']
up_animal = list(map(lambda animal: str.upper(animal), ani))
print("Animal Name in Uppercase = ", up_animal)

number_1 = [1, 2, 3]
number_2 = [4, 5, 6]
result = map(lambda x, y: x + y, number_1, number_2)
print(list(result))

from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print("sum = ", sum)

import functools

lis = [1, 3, 5, 6, 2, ]
# Compute maximum
print("Maximum = ", functools.reduce(lambda a, b: a if a > b else b, lis))

seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))


# How filter() works for iterable list
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)
for s in filtered:
    print("Vowel = ", s)

# Filter method without filter function
randomList = [1, 'a', 0, False, True, '0']
filterList = filter(None, randomList)

print('The Filter elements are : ')
for element in filterList:
    print(element)


# Map() function

# addition map function
def addition(n):
    return n + n


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

#
numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers_1, numbers_2)
print("Sum of two array = ", list(result))


#
def calculationSquare(n):
    return n * n


numbers = (1, 2, 3, 4)
result = map(calculationSquare, numbers)
print(result)

# converting map object to set
numberSquare = set(result)
print(sorted(numberSquare))

# lambda with map
numbers = (1, 2, 3, 4)
result = map(lambda x: x * x, numbers)
print(result)

# converting map object to set
numberSquare = set(result)
print(numberSquare)

# Multiple iterators to map() using lambda
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = map(lambda n1, n2: n1 + n2, num1, num2)
print(list(result))


def myMapFunc(list1, tuple1):
    return list1 + "_" + tuple1


my_list = ['a', 'b', 'c', 'd', 'e']
my_tuple = ('PHP', 'Java', 'Python', 'C++', 'C')

update_list = map(myMapFunc, my_list, my_tuple)
print(update_list)
print(list(update_list))
