#python is uses arithmetic division by default (no remainder), but this is rarely what is required, so we have to import division;
#this changes the \ to decimal divison, but you can get integer division with the \\

#Modules
from __future__ import division
import re
my_regex = re.compile("[0-9]+", re.I)

import re as regex #if there is already a re in the file or if the name of the module is rather long

from collections import defaultdict, Counter #will import the specific value and can be used without the collections.


x = 5/2
y = 5//2

print x, y

for i in [1,2,3,4,5]:
    print i
    for j in [1,2,3,4,5]:
        print i + j
    print i
print "done looping"

list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]

easier_to_read_list_of_lists = [ [1,2,3],
                                 [4,5,6],
                                 [7,8,9]]
#can use a backlash to indicate that a statement continues on the next line

two_plus_three = 2 + \
                 3
#to correctly copy python code with formatting and all, use the %paste function



#Functions

def double(x):
    '''this is where you put and optional docstring that explains what the function does. Ex. multiplies by 2'''
    return x * 2

def apply_to_one(f):
    '''calls the function f with 1 as its argument'''
    return f(1)

my_double = double
x = apply_to_one(my_double)
print x

another_double = lambda x: 2 * x #don't do this
def another_double(x):
    return 2 * x  #do this instead

def my_print(message="my default message"):
    print message
my_print("hello") #prints hello when the function is called and the defined argument is replaced by a new argument
my_print() #no new argument is defined and the defined argument is printed

#Strings
#the backslash allows you to use special characters like tab, and if you want to print a string as is (by printing the backslash, r""
#can be used

#how to print a multi-line string using three double-quotes
multi_line_string = """This is the first line.
and this is the second line.
and this is the third line."""

print multi_line_string

#Exceptions
try:
    print 0/0
except ZeroDivisionError:
    print "cannot divide by zero"

x = range(10)

print x

zero = x[0] #assigns 0 to the zero variable
one = x[1]
nine = x[-1] #assigns the last element to the variable nine
eight = x[-2] #assigns the next the last element to the variable eight

print zero, one, nine, eight

x[0] = -1 #changes the first element (0) to -1

print x

#Use square brackets to "slice" lists

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

#verify list membership

1 in [1,2,3]
0 in [1,2,3]

#Concatenation--change the initial list or create a new list
#adding on to a list

x = [1,2,3]
x.extend([4,5,6])

print x

#extending a list while creating a new list

x = [1,2,3]
y = x + [4,5,6]

print x, y

#adding to a list one element at a time

x = [1,2,3]
x.append(0)

print x

y = x[-1]
z = len(x)

print y, z

#unpack lists

x,y = [1,2]

#if there is a throwaway value

_,y = [1,2]



#Tuples

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print "cannot modify a tuple"

#tuples are a convenient way to return multiple values from functions

def sum_and_product(x,y):
    return (x + y), (x * y)
sp = sum_and_product(2,3)
s, p = sum_and_product(5, 10)

print sp, s, p

#multiple assignment

x, y = 1, 2
x, y = y, x #swapping variables

#Dictionaries

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel" : 80, "Tim" : 95}

#returns values associated with a key

joels_grade = grades["Joel"]

#if a key is asked for that is not present

try:
    kates_grade = grades["Kate"]
except KeyError:
    print "no grade for Kate!"

#to check if a key is in the dictionary
joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

print joel_has_grade, kate_has_grade

#get method

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0) #returns 0 because Kate is not in the dictionary

#assigning key pairs

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades) #assigns the number of keys in the dictionary

print num_students

#dictionaries used to represent structured date

tweet = {"user" : "joelgrus", "test" : "Data Science is Awesome", "retweet_count" : 100, "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]}

tweet_keys = tweet.keys() #list of keys
tweet_values = tweet.values() #list of values
tweet_items = tweet.items() #list of (key, value) tuples

"user" in tweet_keys
"user" in tweet
joelgrus in tweet_values

#counting words in a document
#Method 1:

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
#method 2
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

#method 3

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

from collections import defaultdict

word_counts = defaultdict(int) #produces a 0
for word in document:
    word_counts[word] += 1


dd_list = defaultdict(list) #produces a blank list
dd_list[2].append(1) #dd_list contains {2: [1]}

dd_dict = defaultdict(dict) #produces an empty dictionary
dd_dict["Joel"]["City"] = "Seattle" #{Joel: {"City" : "Seattle"}}

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1 #Now dd_pair contains {2: [0,1]}

#the above are useful when you want to collect values by key and you don't want to check to see if the key exists yet

#Counter--turns a sequence of values into a defaultdict(int)-like object mapping keys to counts (used for histograms)

from collections import Counter
c = Counter([0,1,2,0]) #c is basically {0: 2, 1: 1, 2: 1}

#Sets--represents a collection of distinct elements; sets are used because "in" is a very fast operation in sets or to find distinct elements in a collection

s = set()
s.add(1) #adds 1 to set
s.add(2) #adds 2 to set
s.add(2) #nothing is added because 2 is not a distinct element
x = len(s) #2
y = 2 in s #True
z = 3 in s #False

hundreds_of_other_words = ["100words", "200words"]

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

'zip' in stopwords_list #false, but you would have to check every element

stopwords_set = set(stopwords_list)
'zip' in stopwords_set


item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_list)
distinct_item_list = list(item_set)

print item_set

#Control Flow

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

#ternery if-then-else on one line

parity = "even" if x % 2 == 0 else "odd"

#while loop

x = 0
while x < 10:
    print x, "is less than 10"
    x += 1

#for loops

for x in range (10):
    print x, "is less than 10"

#complex logic using continue and break

for x in range(10):
    if x == 3:
        continue #continues to the next iteration
    if x == 5:
        break  #stops the process
    print x

#Truthiness

one_is_less_than_two = 1 < 2
true_equals_false = True == False

print one_is_less_than_two, true_equals_false

#the value None is used to represent a nonexistent value

x = None

print x == None #True, but not pythonic
print x is None #True and pythonic

s = some_function_that_returns_a_string
if s:
    first_char = s[0]
else:
    first_char = " "

first_char = s and s[0] #a simpler way to accomplish the above, returns its second value when the first is true and the first when it is not

safe_x = x or 0

#the all function returns true when all elements in a list are true, and any which returns true when any element in a list is true

all([True, 1, {3}]) #True
all([True, 1, {}]) #False, b/c {} is false
any([True, 1, {}]) #True, because True is true
all([]) #true, no falsy elements in the list
any([ ]) #false, no true elements in the list

#The Not So Basics

#Sorting; sort will sort the list, sorted will sort a list but create a new list in the process

x = [4,1,2,3]
y = sorted(x)
x.sort()

#sorts from smallest to largest, but this can be changed
#absolute value from largest to smallest

x = sorted([4,1,-2,3], key=abs, reverse=True)
print x

#sort the words and counts from highest to lowest; compares the results of a funtion specified with a key

#wc = sorted(word_counts.items(), key=lambda (word, count): count, reverse=True)



#List Comprehensions; transforms a list into another list by choosing certain elements or transforming elements or both

even_numbers = [x for x in range(5) if x % 2 == 0] #[0,2,4]
squares = [x*x for x in range(5)] #[0,1,4,9,16]
even_squares = [x * x for x in even_numbers] #[0, 4, 16]

#turn lists into dictionaries or sets

square_dict = {x : x * x for x in range(5)} #x {0:0, 1:1, 2:4, 3:9, 4:16}
square_set = {x * x for x in [1, -1]} #{1}

#if you don't need a value from the list, insert an underscore

zeroes = [0 for _ in even_numbers] #has the same length as even_numbers

#list comprehension with multiple fors

pairs = [(x, y)
         for x in range(10)
         for y in range(10)] #will produce 100 pair combinations

#building on earlier fors
#only pairs where x < y, range (lo, hi) equals [lo, lo +1]

increasing_pairs = [(x,y)
                    for x in range(10)
                    for y in range (x + 1), 10]

#Generators and Iterators

#a generator is something that you can iterate over where values are produced only as needed

#def lazy_range(n):
    #"""a lazy version of a range"""
    #i = 0
    #while i < n:
        #yield i
        #i += 1

#def natural_numbers():
    #"""returns 1, 2, 3..."""
    #n = 1
    #while True:
        #yield n
        #n += 1

#can only iterate through once--if you need to iterate multiple times, it will have to be run again or you'd need to use a list

#second way to create generators--for comprehensions wrapped in parentheses

lazy_evens_below_20 = (i for i in lazy_range(20) if 1 % 2 == 0)

#Random Numbers can be generated with the random module

import random

four_uniform_randoms = [random.random() for _ in range(4)]
 #random.random produces numbers uniformly between 0 and 1 and is used most often; is deterministic and random.seed can be set
 #to get a uniform, reproducible set of random numbers

random.seed(10)
print random.random

#randrange produces an element chosen at random from within a range

print random.randrange(10)
print random.randrange(3,6)

#random.shuffle randomly reorders a list

up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

#pick a random element from a list
my_best_friend = random.choice(['Alice', 'Bob', 'Charlie', 'Oscar'])

print my_best_friend

#choosing a random sample without replacement

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print winning_numbers

#choosing a random sample WITH replacement

four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]

#Regular Expressions

#reg expression provide a way for searching text

import re
print all([                     #all of these are true because
    not re.match('a', 'cat'),    #cat does not start with a
    re.search('c', 'cat'),                           #cat has an a in it
    not re.search('c', 'dog'),       #dog doesn't have a c in it
    3 == len(re.split('[ab]', 'carbs')), #split on a or b to ['c', 'r', 's']
    'R-D-' == re.sub('[0-9]', '-', 'R2D2') #replace digits with dashes
])# prints True

#Object Oriented Programming
#member functions are accessed by placing a . after the class, classes are name with PascalCase

class Set:

    #these are member functions
    #every one takes a first parameter (self)
    #that refers to a particular Set object being used

    def __init__(self, values=None):
        """This is the constructor.
        It gets called when you create a new Set.
        You would use it like
        s1 = Set()--empty set
        s2 = Set([1,2,3,4)] initializes with values"""
        self.dict = {} #each instance of Set has its own dict property that will be used to track membership

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """This is a string representation of a Set object if you type it in the Python prompt or pass is to str()"""
        return "Set: " + str(self.dict.keys())

    #membership represented by being a key in self.dict with value True
    def add(self, value):
        self.dict[value] = True

    #value is in the set if it is a key in the dictionary
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

#s and t are instances of the class Set--the values are assigned to the set list

s = Set([1,2,3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)

t = Set([1,2,6,7,8])
t.add(10)
print t.contains(10)
t.remove(6)
print t.contains(6)



#Functional Tools

#curry or partially apply functions to create new functions

def exp(base, power):
    return base ** power

from functools import partial
two_to_the = partial(exp, 2)
print two_to_the(3)

square_of = partial(exp, power = 2)
print square_of(3)

def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs= [double(x) for x in xs] #perform the double(x) function for all the values in the xs list
print twice_xs
four_xs = map(double, twice_xs) #uses the map function to double twice_xs
print four_xs
list_doubler = partial(map, double) #partial function used to double the list
sixteen_xs = list_doubler(four_xs)
print sixteen_xs

#map multiple arguments if there are multiple lists

def multiply(x, y): return x * y

products = map(multiply, [1, 2, 7], [4, 5, 9]) #a list of xs and a list of ys

print products

#filter does the work of a list comprehension if

def is_even(x):
    """True if x is even, false if x is odd"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]
print x_evens
x_evens = filter(is_even, twice_xs)
print x_evens
list_evener = partial(filter, is_even)
x_evens = list_evener(four_xs)
print x_evens

#reduce combines the first two elements of the list with the third, fourth and so on, producing a single result

x_product =reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product = list_product(xs)
print x_product

#enumerate--iterate over a list using its elements and their indexes

documents = [1, 2, 3, 4, 5]
do_something = documents[1] + 1
#not pythonic
for i in range(len(documents)):
    document = documents[i]
    do_something(i, document)

#not pythonic
i = 0
for document in documents:
    do_something(i, document)
    i += 1

#the pythonic solution is to enumerate which produces tuples (index, element)

for i, document in enumerate(documents):
    do_something(i, document)

#if only length of documents is needed

for i in range(len(documents)): do_something(i) #not pythonic
for i, _ in enumerate(documents): do_something(i) #pythonic

#zip and argument unpacking

#zip transforms multiple lists into a single list of tuples of corresponding elements

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list12 = zip(list1, list2)
print list12

#if the lists are different lengths, the zip stops when the first list ends

#unzip lists--the * performs argument unpacking, using the elements of pairs as individual arguments to zip
#argument unpacking can be used with any function

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

print letters, numbers

def add(a, b): return a + b

add(1, 2)
# type error: add([1, 2])
add(*[1, 2]) #list is unpacked by *, so 3 is returned

#args and kwargs

#creates a higher order function that takes as its input "f" and returns a new function that for any input returns twice the value of f
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

#this sometimes works, but it breaks down with functions that take more than a single argument

def f1(x):
    return x + 1

g = doubler(f1)
print g(3)
print g(-1)

def f2(x, y):
    return x + y

#g = double(f2)
#print g(1, 2) #TypeError--g takes one argument and two are given


#specifies a function that takes arbitrary arguments, args is a tuple of its unnamed elements and kwards is a dict of its named arguments
def magic(*args, **kwargs):
    print "unnamed args: ", args
    print "keyword args: ", kwargs

magic(1, 2, key = "word", key2 = "word2")

#args and kwargs to supply a function

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z" : 3}
print other_way_magic(*x_y_list, **z_dict)

def doubler_correct(f):
    """works no matter what type of input f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print g(1, 2)