# 1. Adding Index to Iterables(list, tuples, etc..)
students = ['Immaculate', 'Prisca', 'Lizy']
student_with_index = list(enumerate(students))
print(student_with_index)

# 2. Cumulative summing a sequence of numbers
import numpy as np

factors = list(np.cumsum(range(0, 20, 3)))
print(factors)

# 3. Using all or any in a conditional statement
data = [True, True, False]
if any(data):
    print("at least")

if not all(data):
    print("That's right")

# 4. Iterating over two python list
books = ['mabala', 'money heist', 'GOT']
pages = [200, 300, 600]
for book, page in zip(books, pages):
    print("{}--->{}".format(book, page))

# 5. Unpacking a Python List
names = ['Melisa', 'Lisa', 'Peace']
niece, friend, crush = names
print('{} {} {}'.format(niece, friend, crush))

# 6. Reversing a string in Python
quote = "doog si doG"
print(quote[::-1])

# 7. List comprehension to create a specific list
odd = [x for x in range(20) if x % 2 != 0]
print(odd)

# 8. Merging two dictionaries
a = {"name": "Python", "creator": "Guido"}
b = {"age": 30, "gender": None}
a.update(b)
print(a)

# 9. Create a single string from all elements in the list
python = ["Python", "Syntax", "is", "elegantly"]
python_string = ' '.join(python)
print(python_string)

# 10. Swapping value in Python
FirstName = "Kalebu"
LastName = "Jordan"
FirstName, LastName = LastName, FirstName
print(FirstName, LastName)
