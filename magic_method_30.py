# 1. swap two numbers
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

# 2. Reversing a string in python
a = "hereisastring"
print("Reverse is", a[::-1])

# 3. Create a single string
a = ['let', 'code', 'together']
print(" ".join(a))

# 4. Changing of Comparison Operators
n = 10
result = 1 < n < 20
print(result)
result = 1 > n <= 9
print(result)  # False

# 5. Print The File Path of Imported Modules
import os
import socket

print(os)
print(socket)


# 6. Return Multiple Values From Functions
def x():
    return 1, 2, 3, 4


a, b, c, d = x()
print(a, b, c, d)

# 7. Find The Most Frequent Value In a List
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key=test.count))  # 4

# 8. Check The Memory Usage of An Object
import sys

x = 1
print(sys.getsizeof(x))

# 9. Print String N Times
n = 2
a = "ourcodesolution"
print(a * n)

# 10. Checking if two words are anagrams
from collections import Counter


def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


print(is_anagram('cdab', 'abcd'))  # True
print(is_anagram('jkin', 'nikj'))  # False

# 11. Convert it to a single list without using any loops
import itertools

a = "ourcodesolution"
print(list(itertools.chain.from_iterable(a)))

# 12. Convert list of list into single list
ourlist = [[1, 2], [3, 4], [5, 6]]

lst = list(itertools.chain.from_iterable(ourlist))
print(lst)

# 13. Printing the repeated characters: task is to print the pattern like this Geeeeekkkkss. So we can easily print this pattern without using for loop.
print("A" + "b" * 5 + "c" * 4 + "D" * 2)

# 14.Sorted
data = [3, 5, 1, 10, 9]
sorted_data = sorted(data, reverse=True)
print(sorted_data)

# 15. Dict sorted
data = [
    {"name": "Max", "age": 6},
    {"name": "Lisa", "age": 20},
    {"name": "Ben", "age": 9},
]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)

# 16. store unique values insets
my_list = [1, 2, 3, 4, 5, 6, 7, 7, 7]
my_set = set(my_list)
print(my_set)

# 17. save memory with generators
import sys

my_list = [i for i in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list), bytes)

my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")

# 18. define default values in dict with .get() or .defaults
my_dict = {'item': 'football', 'price': 10.00}
count = my_dict.get('count', 0)
print(count)

count = my_dict.setdefault('count', 0)
print(count)

# 19. count hashable objects with collections.counter
from collections import Counter

my_list = [10, 10, 10, 10, 5, 5, 2, 9, 9, 9, 9, 9]
counter = Counter(my_list)
print(counter)
print(counter[10])
print(counter[3])

most_common = counter.most_common(2)
print(most_common)

# 20. Marge Two dict
d1 = {"name": "alex", "age": 25}
d2 = {"name": "alex", "city": "mumbai"}
merged_dict = {**d1, **d2}
print(merged_dict)

# 21. Use all and any in python
sub = 2500
likes = 200
comment = 50
condition = [
    sub > 150, likes > 150, comment > 50
]
if all(condition):
    print("Hi All")

if any(condition):
    print("Hi Nova")

# 22. check the occurrence of a number in the list
a = [1, 3, 4, 6, 7, 8, 3, 2, 12, 2, 2, 5, 6, 7, 1, 1, 2, 4]
a = max(set(a), key=a.count)
print(a)

# 23. Check palindrome
name = 'test'
ispalindrome = name.find(name[::-1]) == 0
print(ispalindrome)
name = '121'
ispalindrome = name.find(name[::-1]) == 0
print(ispalindrome)

# 24. Python Threading
import threading
import time


def thread_function(name):
    print("Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")


my_thread = threading.Thread(target=thread_function, args=(1,))
my_thread.start()
time.sleep(1)
my_second_thread = threading.Thread(target=thread_function, args=(2,))
my_second_thread.start()
my_second_thread.join()

# 25. Ternary Operator
isHappy = True
result_string = 'Happy' if isHappy else 'Not Happy'
print(result_string)  # Happy

# 26. Fizz Buzz Program
# 1)
for i in range(100):
    if (i % 15 == 0):
        print("fizzbuzz")
    elif (i % 5 == 0):
        print("buzz")
    elif (i % 3 == 0):
        print("fizz")
    else:
        print(i)


# 2)
# for i in range(100):
#     d=''
#     if(i%3==0) {d+="fizz"}
#     if(i%5==0) {d+="buzz"}
#     if(d==''):
#         print(i)
#     else:
#         print(d)


# 3)
# c3=0
# c5=0
# for i in range(100):
#     c3++;
#     c5++;
#     d=''
#     if(c3==3) { d+="fizz"; c3=0}
#     if(c5==5) { d+="buzz"; c5=0}
#     if(d==''):
#         print(i)
#     else:
#         print(d)

# 27. Vowel remover program
def vowel_remover(text):
    string = ""
    for l in text:
        if l.lower() != "a" and l.lower() != "e" and l.lower() != "i" and l.lower() != "o" and l.lower() != "u":
            string += l
    return string


print(vowel_remover("hello world!"))

# 28. random number and string generate
# import string
# import random
#
# N = 15
# ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
# output:  # OJ2YJYKV7PKL47D
#
# rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
# s = rand_str(10)
# output:  # zdszkbjryt
#
# import random, string
#
#
# def randomword(length):
#     return ''.join(random.choice(string.lowercase) for i in range(length))
#
#
# randomword(10)
#
# import random, string
#
#
# def randomword(length):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(length))


# 29. external ip address program
# if you needed to know what is your external ip address.
#
# import urllib
# import re
#
# print ("we will try to open this url, in order to get IP Address")
#
# url = "http://checkip.dyndns.org"
#
# print (url)
#
# request = urllib.urlopen(url).read()
#
# theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)
#
# print ("your IP Address is: ",  theIP)

# 30. Find specific file in python
# import os
#
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))
#
# find
# all
# mp3
# files in root
# directory
# path.
# import fnmatch
# import os
#
# rootPath = '/'
# pattern = '*.mp3'
#
# for root, dirs, files in os.walk(rootPath):
#     for filename in fnmatch.filter(files, pattern):
#         print(os.path.join(root, filename))
#
# this
# example
# filter
# all
# images
# files in the
# system.
# import fnmatch
# import os
#
# images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
# matches = []
#
# for root, dirnames, filenames in os.walk("C:\"):"
#                                          "for extensions in images:
#     for filename in fnmatch.filter(filenames, extensions):\
#         matches.append(os.path.join(root, filename))