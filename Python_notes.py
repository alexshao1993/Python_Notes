# Basic Math
print(6 / 2)         # = 3.0    Division always returns float
print(2**3)          # = 8      Exponentiation
print(10 % 3)        # = 1      Modulo (Remainder)
print(10 // 3)       # = 3      Integer Division (opposite of modulo)

# Naming Conventions
snake_case = 1
SNAKE_CASE_PI = 3.14        # Constants use capital case
UpperCamelCase = 'class'    # refers to a class
__no_touchy__ = 1           # dunder refers to private

# String Escape Characters
new_line = "hello \n world"
str = "he said \"ha ha\""   # he said "ha ha"

# Formatting Strings
# F-strings
x = 10
formatted = f"I've told you {x} times already!"  # I've told you 10 times already
formatted = f"I've told you {x + 10} times already!"  # I've told you 10 times already
# .format method
formatted = "I've told you {} times already!".format(10)  # I've told you 10 times already
# % operator
formatted = "I've told you %d times already!" % x  # I've told you 10 times already

# User input
color = input("What's your favorite color?")

# Truthiness
x = 1
x is 1  # True -> Truthy
x is 0  # False -> Falsy

# empty objects, strings, None, zero are by default FALSY
animal = ""
if animal:
    print(animal)

# is vs "=="
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True, checking values
a is b  # False, checking memory location

# Ranges
range(7)            # 0-6
range(1, 8)         # 1-7
range(1, 10, 2)     # 1, 3, 5, 7, 9
range(7, 0, -1)     # 7-1

# Lists Methods
first_list = [1, 2, 3, 4]
first_list.append(5)            # Only accepts 1 item
first_list.extend([6, 7, 8])    # Joins the list together, more than 1 item
first_list.insert(1, 'Hi!')     # Inserts at index 1
first_list.clear()              # Clears entire list

first_list = [1, 2, 3, 4]
first_list.pop()                # Remove last item by default [1,2,3], and returns 4
first_list.pop(1)               # Removes index 1, [1,3,4] returns 2

value = 4
first_list.remove(value)        # Removes the 1st item matching the value, does not return

numbers = [5, 5, 6, 7, 8, 9, 10]
numbers.index(5)                # 0, returns the 1st instance index
start_index = 1
end_index = 5
numbers.index(5, start_index, end_index)    # 1, start_index is inclusive,
numbers.count(5)                            # 2, count of the value
numbers.reverse()                           # reverse the order of list, does NOT return list
numbers.sort()                              # sort in ascending order, does NOT return list
' '.join(numbers)                           # join list into a string with space between items

# List Slicing
first_list = [1, 2, 3, 4]
sliced_list = first_list[start:stop:step]
first_list[1:]                              # [2, 3, 4]
first_list[-1:]                             # [4]
first_list[:]                               # [1, 2, 3, 4]

# Slice end index is exclusive counting
first_list[:2]                              # [1, 2]
first_list[1::2]                            # [2, 4]
first_list[::2]                             # [1, 3]

# Reverse step
first_list[1::-1]                           # [2, 1]
first_list[:1:-1]                           # [4, 3]
first_list[2::-1]                           # [3, 2, 1]

# Swapping values in list
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names)                                # ["Michelle", "James"]

# List Comprehension
nums = [1, 2, 3]
[x * 10 for x in nums]              # [10, 20, 30]
[num * 10 for num in range(1, 6)]    # [10. 20. 30. 40, 50]

numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]                    # [2, 4, 6]
odds = [num for num in numbers if num % 2 == 1]                     # [1, 3, 5]
weird = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]   # [0.5, 4, 1.5, 8, 2.5, 12]

# Nested List Comprehension
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(val) for val in l] for l in nested_list]    # 1, 2, 3, 4, 5, 6, 7, 8, 9

# Dictionary
cat = {"name": "blue",
       "age": 3.5,
       "isCute": True}
cat2 = dict(name="kitty", age=0.5)

# Create a dict using 2 lists
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)

for value in cat.values():
    print(value)

for key in cat.keys():
    print(key)

for key, value in cat.items():
    print(key, value)

# Test existence of key in dictionary
"name" in cat       # True
"dogs" in cat       # False

cat.clear()             # empties dictionary
cat3 = cat.copy()       # creates a unique object that's a duplicate

# Creates key-value pairs from comma seperated values:
{}.fromkeys(["email", "name", "profile bio"], "unknown")       # Create default values {'email': 'unknown', 'name': 'unknown', 'profile bio': 'unknown'}
#           Iterable object                   Value
{}.fromkeys(range(0, 10), "unknown")

cat.get('no_key')       # Retrieves a key in an object, returns None if not found
cat.pop("isCute")       # removes isCute key and return True
cat.popitem()           # removes random key-value pair, return the key-value pair removed

cat4 = {'city': "LA"}
cat4.update(cat)        # add/update key-value pairs from cat, and add them to cat4

# Dictionary Comprehension
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}  # {'first': 1, 'second': 2, 'third': 9}
{num: num**2 for num in [1, 2, 3, 4, 5]}                               # {1:1, 2:4, 3:9, 4:16, 5:25}

# Tuple
a_tuple = (1, 2, 3, 3, 4, 5)
value = (1,)        # Creates a tuple with only 1 value
# Faster then lists
# Can be used as keys in a dictionary
a_tuple.count(3)    # 2
a_tuple.index(1)    # 0

# Set
# No duplicates
# Not ordered
# Cannot access items by index
s = {1, 4, 5}
s = set({1, 4, 4, 5})   # {1, 4, 5}
4 in s                  # True
s = {1, 4, 5, 'a', 'b', 23.33334}   # can include different types
s.add(6)
s.remove('c')       # Error if item not found
s.discard('c')      # No error
s1 = s.copy()
s.clear()

# Set math
s1 = [1, 2, 3, 4, 5, 6]
s2 = [2, 3, 4, 6, 7]
s_union = s1 | s2           # [1, 2, 3, 4, 5, 6, 7]
s_intersection = s1 & s2    # [2, 3, 4, 6]

# Set Comprehension
{x**2 for x in range(10)}   # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# Function


def name_of_function():
    return "Hi!"


from random import random


def flip_coin():
    r = random()        # Generate a random float between 0 - 1
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

# Parameter is in declaration
# Argument is passsed into a parameter


def is_odd_number(num):
    if num % 2 != 0:
        return True         # No need for ELSE
    return False


def exponent(num, power=2):  # power defaults to 1
    return num**power

# default param can be a function


def add(a, b):
    return a + b


def math(a, b, fn=add):
    return fn(a, b)


def full_name(first, last):
    return "Your name is {first} {last}"


full_name(first="Alex", last="Shao")
full_name(last="Shao", first="Alex")  # Keyword Arguments allows reordering of params

# Scope
total = 0


def sum():
    global total        # references variable outside the function
    total += 1
    return total


def outer():
    count = 0

    def inner():
        nonlocal count  # access variable in nested function
        count += 1
        return count
    return inner()


def say_hello():
    """ Docstring for documentation """
    return 0


say_hello.__doc__  # return the Docstring

# *args
# Gathers remaining arguments as a tuple


def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3


def sum_all_nums(*args):
    print(args)


sum_all_nums(4, 6, 8, 9)  # (4,6,8,9)


def sum_all_nums(num1, *args):  # This works as well
    print(num1, args)

# **kwargs
# keyword arguments
# gathers remaining keyword arguments as a dictionary


def fav_colors(colt="purple", ruby="red", ethel="teal"):
    print(colt, ruby, ethel)


def fav_colors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

# Parameter Ordering
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

# Tuple unpacking


def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)


nums = [1, 2, 3, 4, 5, 6]
sum_all_values(*nums)       # * unpacks the list into a tuple
colors = {"colt": "purple", "ruby": "red", "ethel": "teal"}
fav_colors(*colors)         # ** unpacks a dictionary into a tuple

# Lambdas
# pass function into a parameter
def square(num): return num ** num
square2 = lambda num: num*num
#                1 param: returns num*num
square2.__name__    # <lambda>

# Map
# accepts at least 2 arguments, a function and an iterable
# runs the function (typically a lambda) for each item in the iterable and return a map object
nums = [2, 4, 6, 8, 10]
doubles = map(lambda x: x * 2, nums)
list(doubles)   # [4, 8, 12, 16, 20]

people = ["Darcy", "Christina", "Dana", " Annabel"]
peeps = map(lambda name: name.upper(), people)
list(peeps)     # upper case people names

# Filter
l = [1, 2, 3, 4]
# return values that return true to the lambda
evens = list(filter(lambda x: x % 2 ==0, l))    # [2, 4]
#                   lambda,              iterable

# Combing map and filter
users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(),
    filter(lambda u: not u['tweets'], users)))

# all
# Takes all elements in the iterable, and return T if all elements are truthy
l1 = [1, 2, 3, 4]
l2 = [0, 1, 2, 3]
all(l1)     # True
all(l2)     # False

people = ["Charlie", "Casey", "Cody"]
all([name[0]=="C" for name in people])  # True, Check if all names start with C


# any
# Takes all elements in the iterable, and return T if any elements are truthy
nums = [2, 60, 26, 18, 21]
all([num % 2 == 0 for num in nums]) # False, check if all numbers are even
any([num % 2 == 0 for num in nums]) # True, check if any numbers are even

all(num % 2 == 0 for num in nums)   # Works as well as a generator

# sorted
# returns a sorted list from the items in iterable
nums = [6, 1, 8, 2]
sorted(nums)                # [1, 2, 6, 8]
sorted(nums, reverse=True)  # [8, 6, 2, 1]


users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
sorted(users, key=lambda user: user['username'])    # sort using username


# max/min
# Takes multiple arguments, or an iterable, returns the max/min
max(names, key=lambda n: len(n))    # similar to sorted, takes a key argument

# reversed
# return a reversed iterator object
for char in reversed("hello world"):
    print(char)     # if you just need to reverse a list

# len
'hello'.__len__()   # built in function

# abs
# returns absolute value of a number
abs(-10)    # 10

# sum
sum([1, 2, 3])  # 6
sum([1, 2, 3], 10)  # 6 + 10 = 16
#   iterable,  start

# round
round(10.2)     # 10
round(10.12356, 2)  # 10.12
#     num,      num of digits
round(10.12356, None)  # 10 round to int

# zip
first_zip = zip([1,2,3], [4,5,6])   # (1,4), (2,5), (3,6)
uneven_zip = zip([1,2,3], [4,5,6,7,8])   # (1,4), (2,5), (3,6) stops zipping when out of elements

five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
list(zip(*five_by_two)) # *reverses the zip and unpacks the tuples
                        # [(0,1,2,3,4), (1,2,3,4,5)]

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

[max(pair) for pai in zip(midterms, finals)]    # [98, 91, 78] picks the max out of midterms and finals
{t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}   # picks the max out of midterms and finals for each student
                                                                   # {'dan': 98, 'ang':91, 'kate':78}

scores = map(
            lambda pair: max(pair),
            zip(midterms, finals)
            )   # [98, 91, 78]

scores = zip(
            students,
            map(
                lambda pair: max(pair),
                zip(midterms, finals)
                )
            )   # zip student name and the max score
print(dict(scores)) # {'dan': 98, 'ang':91, 'kate':78}

# Debugging and Error Handling
# Common errors
# SyntaxError
# NameError:        variable is not defined
# TypeError:        operation or function for a wrong type
# IndexError:       invalid index
# ValueError:       function receives an right type but wrong value
# KeyError:         key does not exist in dictionary
# AttributeError:   does not contain attribute

# Raise your own exception
raise ValueError('invalid value')

try:
    num = int(input("please enter a number: "))
except:
    print("That's not a number!")
else:
    print("Runs when no exceptions occured")
finally:
    print("Runs no matter what")

# pdb
import pdb
pdb.set_trace()

# PDB commands:
# l (list) -> shows where you are in code
# n (next line)
# p (print)
# c (continue - finishes debugging)

# can type variable name to see value

# if variable name conflict with command,use
# p c
# print variable_name

# Modules
# Keep Python files small
import random

fruits = ['apple', 'banana', 'cherry', 'durian']
print(random.choice(fruits))    # random element from list
print(random.shuffle(fruits))   # random order list

import random as omg_so_random # alias for module

# import parts of a module, only import what you need
from random import choice, randint
from random import choice as picks, randint # give alias with from import
from random import * # import everything
print(choice(fruits))
print(shuffle(fruits))

# custom modules
import python_file_name

# pip
python3 -m pip install NAME_OF_PACKAGE

# __name__
# if the file is the main file being run, its value is "__main__"
# file is ran on import, to prevent this
if __name__ == "__main__":
    # this code will only run if the file is the main file!

# OOP
# Class - a blueprint for objects
# instance - objects that are constructed from a class
# Encapsulation: grouping of public and private attributes and methods into a programmatic class
# Abstraction - only exposing relevant data
class User: # class name are usually use CamelCase
    pass

user1 = User()  # creating an instance of a class

# __init__
class User:
    def __init__(self, first, last, age): # self refers to the instance of class
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):    # gives acess to self
        return f"{self.first} {self.last}"

user1 = User("Joe", "Smith", 68)
user1.full_name()   # Joe Smith

# _name -> indicates private
# __name -> changes to _ClassName__name
# __name__ -> used for python specific methods

# Class attributes -> shared by all instances
class User:

    active_users = 0    # class attribute

    @classmethod                # next method will be a class method
    def display_active_user(cls):
        print(cls.active_users) # use cls to reference the class

    def __init__(self, first, last, age): # self refers to the instance of class
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1            # addressed without self

    def __repr__(self):         # represents the instance, used in str()
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has left"

    def full_name(self):    # gives acess to self
        return f"{self.first} {self.last}"



class Pet:
    allowed = ["cat", "dog", "fish", "rat"]     # class attribute

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            self.allowed = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

# id
id(cat.allowed) # returns the python ID in memory

# Inheritance
# Define a class which inherits from another class
class Animal:
    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Aniaml): # Pass parent class as an argument
    pass

blue = Cat()

isinstance(blue, Cat) # True, checks if blue is a Cat

# Property
class Human:
    def __init__(self, first, last ,age):
        self.first = first
        self.last = last

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")

jane = Human("Jane", "Goodall", 34)

# super
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Aniaml): # Pass parent class as an argument
    def __init__(self, name, breed, toy):
        # Animal.__init__(name, species="Cat")
        super().__init__(name, species="Cat") # inits parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

# Multiple Inheritance
class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        super().__init__(name=name) # super here refers to Ambulatory, which ever comes 1st
        Aquatic.__init__(self, name=name)   # self is nessesary when not using super()

# Method Resolution Order (MRO)
Penguin.__mro__
Penguin.mro()
help(Penguin)

class A:
    def do_something(self):
        print("Method Defined In: A")


class B(A):
    def do_something(self):
        print("Method Defined In: B")


class C(A):
    def do_something(self):
        print("Method Defined In: C")


class D(B, C):
    def do_something(self):
        print("Method Defined In: D")
        super().do_something()  # calls B


thing = D()
thing.do_something()
print(D.mro())      # prints class D's MRO

#       A
#     /  \
#    B    C
#    \   /
#      D
#  D,B,C,A,Object

# Polymorphism
# 1) same class method works in a similar way for different classses
# 2) same operation works for different kinds of objects

# method overriding
class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")    # Enforce implementation

class Dog(Aniaml):
    def speak(self):
        return "woof"

class Cat(Aniaml):
    def speak(self):
        return "meow"

# special methods
8 + 2       # 10
"8" + "2"   # "82"
# uses __add__() method on the first(left) operand

from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        raise TypeError("You can't add that!")

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]           # copy() clones the instance
        raise TypeError("You can't multiply that!")

j = Human("Jenny", "Larson", 47)
k = Human("Kevin", "Jones", 49)
print(j + k)    # defined __add___ which would create a new instance of Human

# Inherits dict
class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key): # when key is missing
        print(f"YOU WANT {key}? WELL IT AINT HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE...")
        super().__setitem__(key, value)


# Iterator
# Iterator - an object that can be iterated upon
# Iterable - an object that returns an iterator
"HELLO"         # iterable
iter("HELLO")   # iterator
# next() returns the next item in the iterator, until it raises a StopIteration error

# Custom for loop
def my_for(iterable):
    iterator = iter(iterable, func) # creates an iterator
    while True:
        try:
            i = next(iterator)      # iterate over the iterator
        except StopIteration:
            break
        else:
            func(i)

# custom range() iterator
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self): # required for an iterable
        return self

    def __next__(self): # required for an iterable
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration # must raise error to avoid infinite loop

# Generator
# uses yield, can yield multiple times
# when invoked, returns a generator
def count_up_to(max):    # generator functio that creates a generator
    count = 1
    while count <= max:
        yield count      # stops here for each iteration
        count += 1       # continues here in next iteration

counter = count_up_to(5) # generator created
next(counter)            # iterating over a generator

for num in counter:      # can be iterated
    print(num)

# Infinite Generator
def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

# Generator expression
def nums():
    for num in range(1, 10):
        yield num
g = nums()
g = (num for num in range(1,10))        # uses () instead of [] as in list expression
l = [num for num in range(1,10)]        # list expression
sum(g)
sum(l)                                  # slow due to storing entire list

# Decorator

# we can pass funcs as args to other funcs
def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x * x

print(sum(3, square)) # 1+4+9 = 14


# Decorators are functions
# wraps other functions and enhance their behavior
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a nice day!")
    return wrapper

@be_polite  # decorator syntax
def greet():
    print("My name is Matt")
# greet = be_polite(greet)

# Decorator Pattern
from functools import wraps

def my_decorator(fn):
    @wraps(fn)          # preserves metadata. Ex: __name__, __doc__
    def wrapper(*args, **kwargs):
        # do some stuf with fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return wrapper

# Speed test decorator example
from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums():
    return sum(x for x in range(100000000))
print(sum_nums)

def ensure_no_kwargs(fn):   # does not allow kwargs in fn
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed")
        return fn(*args, **kwargs)
    return wrapper

# ex:
@decorator
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator(func)

# When passing arg into decorator
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator_with_args(arg)(func)

# Ensure first arg is __ example
from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

# Testing
# Test Driven Development
# 1) Write test
# 2) Develop
# 3) If test pass, done!

# Red, Green, Refactor
# 1) Red - Write a test that fails
# 2) Green - Write the minimal amouont of code necessary to make the test pass
# 3) Refactor - Clean up the code

