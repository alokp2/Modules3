
#Modules 3

'''1.What is List? How will you reverse a list?
List is a collection of data type which contains similar and dis-similar data elements at single location.List is mutable,orderable,and indexable.
'''
'''
2.How will you remove last object from a list? 
We can use the del operator to delete the last element using index. Further, we can use the pop() method to remove the last element.
Here are the example.
'''
l = [1, 2, 3, 4]
del l[-1]
print(l)

li = [12, 3, 4, 5, 6, 7]
li.pop()
print(li)

'''Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 
 list1[-1] = 25. we can check it further
'''
li3 = [2, 33, 222, 14, 25]
print(li3)
print(li3[-1])

'''3.Differentiate between append () and extend () methods? 
Append only add one element to the list and Extend can multiple elements at a time to the list.
 '''

'''Write a Python function to get the largest number, smallest num and sum
of all from a list. 
'''
total = 0
list5 = [12, 23, 21, 22, 11, 2, 34, 34, 56, 43]


def largest_num():
    print(max(list5))


def smallest_num():
    print(min(list5))


def total_sum():
    print("Total sum: ", sum(list5))


largest_num()
smallest_num()
total_sum()
'''How will you compare two lists? 
we can compare the two list using condition statement
'''
l1 = [1, 2, 677, 8, 9, 0]
l2 = [2, 3, 4, 5, 6, 7, 8]
if li == l2:
    print("l1 and l1 are equal")
else:
    print("l1 and l2 are not equal")

'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings
'''
count = 0
words = ["Apple", "Banana", "pears", "GrapeG", "hellh"]

for i in words:
    if len(i) > 0 and i[0] == i[-1]:
        count = count + 1

print(count)

'Write a Python program to remove duplicates from a list.'
list3 = [1, 2, 3, 4, 5, 7, 5, 2, 4]

list4 = []
for item in list3:
    if item not in list4:
        list4.append(item)
print(list4)

'''Write a Python program to check a list is empty or not'''
li = []
if not li:
    print("List is empty")
else:
    print("List is not empty")

'''Write a Python function that takes two lists and returns true if they have
at least one common member.'''


def common_member(list6, list7):
    status = True
    for i in list6:
        for j in list7:
            if x == y:
                return status
            else:
                status = True
                return True


x = [1, 2, 3, 4]
y = [1, 2, 5, 6, 7]
print(common_member(x, y))

'''Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.'''


def generatevalues():
    li = list()
    for items in range(1, 10):
        li.append(pow(items, 2))
    print(li[:5])  # for the first five elements
    print(li[-5:])  # for the last five elements


generatevalues()

'''Write a Python function that takes a list and returns a new list with unique
elements of the first list. '''


def new_list_with_unique(list):
    li = []
    for items in list:
        if items not in li:
            li.append(items)
    return li


print(new_list_with_unique([1, 25, 67, 8, 2, 3, 4, 5, 6, 7, 25]))

'''Write a Python program to convert a list of characters into a string. '''


def convertcharcterstostring(items):
    newstring = ""
    for items in items:
        newstring = newstring + items
    return newstring


items = ['T', 'o', 'p', 'T', 'e', 'c', 'h']
print(convertcharcterstostring(items))

'''Write a Python program to select an item randomly from a list'''
import random

list = [1, 2, 3, 4, 5, 6, 7]
k = random.choice(list)
print(k)

'''Write a Python program to get unique values from a list'''
list = [10, 20, 30, 10, 20, 40, 50]
li = []
for items in list:
    if items not in li:
        li.append(items)
print(li)

'''Write a Python program to check whether a list contains a sub list'''

'''Write a Python program to split a list into different variables. '''

list7 = [1, 2, 5, 6]
a, b, c, d = list7
print(a, b, c, d)

''' What is tuple? Difference between list and tuple. 

tuple is a collection data type. Tuple is indexable,orderable and immutable.
It is represented by (). The difference is that the list is represented by [] and list is mutable(changeable).
'''

''' Write a Python program to create a tuple with different data types. 

'''
tuple1 = (1, 2, 'Name', '2.5')
print(tuple1)
print(type(tuple1))

'''Write a Python program to create a tuple with numbers. '''
t = (1, 2, 3, 4, 5, 6)
print(t)

'''Write a Python program to convert a tuple to a string. '''
t2 = (1.2, 3, 4, 5, "string")
print(type(str(t2)))
print(type(t2))

'''Write a Python program to check whether an element exists within a
tuple'''

t3 = ("a", 1, 2, 3, "books", "banana", "box")
if "books" in t3:
    print("True")

else:
    print("False")

'''Write a Python program to find the length of a tuple. '''
print(len(t3))

'''Write a Python program to convert a list to a tuple. '''

list8 = [12, 1, 2, 3, 4, 5, "w"]
t4 = tuple(list8)
print(t4)

'''Write a Python program to reverse a tuple. '''


def reverse_tuple(tuples):
    reverse = tuples[::-1]
    return reverse


print(reverse_tuple(t4))

'''Write a Python program to replace last value of tuples in a list. '''
t5 = (1, 4, 5, 6, 7, 8, 9, 4)
print(t5)

'''Write a Python program to find the repeated items of a tuple.'''

for items in t5:
    if (t5.count(items)) > 1:
        print(items)

'''Write a Python program to remove an empty tuple(s) from a list of tuples. '''
t7 = [(1, 2, '', 4, 5, 6, 7)]
for t in t7:
    if t != '':
        print(t)
'''Write a Python program to unzip a list of tuples into individual lists. '''
my_list = [(1, 'a'), (2, 'b'), (3, 'c')]

num, letter = zip(*my_list)

print("num:", num)
print("letter:", letter)

'''Write a Python program to convert a list of tuples into a dictionary.'''
lists3 = [('x', 1), ('y', 2), ('z', 3)]

for key, value in my_list:
    print(key, value)
mydict = dict(lists3)
print(mydict)

'''How will you create a dictionary using tuples in python? '''
tuples3 = [(1, "apple"), (2, 'banana'), (3, 'grapes')]
for key, values in tuples3:
    print((f"{key},{values}"))
my_dict = dict(tuples3)
print(my_dict)

'''Write a Python script to sort (ascending and descending) a dictionary by
value.'''
dict1 = {1: 3, 4: 6}
dict2 = {7: 10, 10: 13}

'''Write a Python script to concatenate following dictionaries to create a
new one.'''

dict1 = {1: 2, 4: 5}
dict2 = {6: 7, 8: 10}

dict3 = {}
for dict4 in (dict1, dict2):
    dict3.update(dict4)
print(dict4)

'''Write a Python script to check if a given key already exists in a
dictionary'''
dict5 = {'name': 'Ramesh', 'age': '25', 'Subject': 'Math'}
check = input("Enter the key:")

if check in dict5:
    print(f"The key '{check}' exists")

else:
    print(f"The key '{check}' does not exist")

'''How Do You Traverse Through A Dictionary Object In Python? '''

dict7 = {'Gujarat': 'Gandhinagar', "chatishgarh": "raipur", "Rajasthan": "jaipur", "Madhya Pradesh": "Bhopal"}

for key, values in dict7.items():
    print(key, values)

'''Write a Python script to print a dictionary where the keys are numbers
between 1 and 15.'''

my_dict = {}
for i in range(1, 15 + 1):
    my_dict[i] = i
print(my_dict)

'''Write a Python program to check multiple keys exists in a dictionary'''


def multiple_key(dicts, keys):
    for key in dicts:
        if key in keys:
            return True
        else:
            return False


dicts1 = {'apple': "1", 'banana': "2"}
key1 = {"apple", "banana"}

if multiple_key(dicts1, key1):
    print("keys exist")

else:
    print("keys does not exist")

'''Write a Python script to merge two Python dictionaries'''

dicts_class = {"1": "Science", "2": "Mathematics", "3": "Social Science"}
dict_student = {'name': 'Ramesh', 'age': '25', 'Subject': 'Math'}

d = dicts_class.copy()
d.update(dict_student)
print(d)

''' Write a Python program to map two lists into a dictionary '''

l1 = [1, 2, 3, 4, 5]
l2 = [10, 11, 12, 14, 15]

dict_list = dict(zip(l1, l2))
print(dict_list)

'''Write a Python program to combine two dictionary adding values for
common keys.'''

dic3 = {'a': 100, 'b': 200, 'c': 300, 'd': 500}
dic4 = {'a': 200, 'b': 300, 'c': 500}

dict_list1 = {}

for key in dic3:
    if key in dict_list1:
        dict_list1[key] += dic3[key]
    else:
        dict_list1[key] = dic3[key]

for key in dic4:
    if key in dict_list1:
        dict_list1[key] += dic4[key]
    else:
        dict_list1[key] = dic4[key]
print(dict_list1)

'''Write a Python program to print all unique values in a dictionary. '''
dic5 = {'a': 2, 'b': 3, 'c': 4, 'd': 4}
unique = set()
for values in dic5.values():
    unique.add(values)

for values in unique:
    print(values)

'''Why Do You Use the Zip () Method in Python? '''
'''zip() returns a zip object which is an iterator of tuples where the first item in each passed iterator is paired together.'''

'''Write a Python function to calculate the factorial of a number (a
nonnegative integer) '''


def calculate_factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)


print(calculate_factorial(7))

'''Write a Python function to check whether a number is in a given range'''


def check_num(num):
    if num > 10 and num < 15:
        print("num is in a range")
    else:
        print("num is not in a range")


check_num(14)

''' Write a Python function to check whether a number is perfect or not. '''


def perfect_value(num):
    f = []
    for item in range(1, num):
        if num % item == 0:
            f.append(item)
    if sum(f) == num:
        return True
    else:
        return False


print(perfect_value(4))

'''Write a Python function that checks whether a passed string is
palindrome or not '''


def palindromes(word):
    p = bool(word.find(word[::-1]) + 1)
    print(p)


palindromes('reviver')

'''How Many Basic Types Of Functions Are Available In Python? '''
'''Two types:pre-built in function and user-defined function'''

'''How can you pick a random item from a list or tuple? '''
lists = [1, 2, 4, 6, 10, 20]
print(random.choice(lists))

'''How can you pick a random item from a range? '''
value = random.randrange(1, 20)
print(value)

'''How can you get a random number in python? '''
items1 = random.randint(1, 40)
print(items1)

'''How will you set the starting value in generating random numbers? '''

'''We can use the seed() function which generates the same random numbers on multiple execution.'''

'''How will you randomizes the items of a list in place? '''
'''By using shuffle method to randomize the list of items in a place.'''

'''Write a Python program to convert degree to radian '''

import math


def degreetoredian(degree):
    return degree * math.pi / 180


print(degreetoredian(90))

'''Write a Python program to calculate the area of a trapezoid '''


def calculate_trapezoid(base1, base2, height):
    return 1 / 2 * (base1 + base2) * height


print(calculate_trapezoid(12, 13, 3))

'''Write a Python program to calculate the area of a parallelogram '''


def parallelogram(b, h):
    return b * h


parallelogram(12, 13)

'''Write a Python program to calculate surface volume and area of a
cylinder'''


def surface_area_cyclinder(r, h):
    return 2 * math.pi * r * (r + h)


print(surface_area_cyclinder(1, 4))


def volume_of_cyclinder(r, h):
    return math.pi * r ** 2 * h


print(volume_of_cyclinder(12, 3))

''' Write a Python program to returns sum of all divisors of a number '''


def sum_divisor(n):
    lists_divisor = []
    for i in range(1, n):
        if n % i == 0:
            lists_divisor.append(i)
    return sum(lists_divisor)


print(sum_divisor(10))
'''Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers'''


def max_min(n):
    max_n = max(n)
    min_n = min(n)
    return max_n, min_n


list_num = [12.5, 11.2, 10.2, 9.5, 8.5, 7.5, 6.2, 5.5, 4.5, 2.2, 1.5, 2.3]
print(max_min(list_num))
