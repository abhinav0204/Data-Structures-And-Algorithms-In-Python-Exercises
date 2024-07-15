## Day 1

""" print("Hello World")
print(5)
 """
## Day 2

## Day 3

# modules - code library written by  external sources or internally in python

# pip -  it can be used as apackage manager  to import modules which downloads from the internet ex - pandas

# import pandas

# pip3 install numpy

## Day 4

""" print("Hello World")
print(5)
print("Bye")
print(17*13)
 """
## Day 5

# commments - used to explain a block of code
#  cntrl + / - comment/uncomment in vs code

# multi line comments - triple single or triple double quotes
# shortcut - alt + shift + A


""" Hey Abhinav

Author : Ambuj

Course : Python-Revision
 """
# Escape sequence - to insert characters that cannot be directly used in a string,we can use escape sequence
""" 
print('Hey i am a \"good boy\' \n this viewer is also a good boy/girl')

print("Hey",6,7,sep='~',end="099")
print("Abhinav") """

## Day 6

# variables - it's like a container that holds data


# data type  - specifies the type of data a variable holds

""" a = 12345
print(type(a))

b = "Abhinav"
print(type(b))

c = True
print(type(c))

d = None
print(type(d))

e = complex(8,2)
print(e,type(e))

print("The type of a is ", type(a))

 """

# everything in python is an object


## Day 7

# operators

# +, - , % , / , //
""" 
print(5+6)
print(15-6)
print(15*6)
print(15/6) # float division
print(15//6) # integer division
print(2**3) # power , exponential
print(2^3) # xor
 """

# calculator
""" 
def calculator(num1,num2,operation):
    if operation == '+':
        return f"The addition of {num1} and {num2} is {num1+num2}"
    
    elif operation == '-':
        return f"The substraction of {num1} and {num2} is {num1-num2}"
    
    elif operation == '*':
        return f"The mutiplication of {num1} and {num2} is {num1*num2}"

    elif operation == '/':
        return f"The float division of {num1} and {num2} is {num1/num2}"
    
    elif operation == '//':
        return f"The integer division of {num1} and {num2} is {num1//num2}"
    
    elif operation == '**':
        return f"The power of {num1} to the raise {num2} is {num1**num2}"
    
    else:
        return "Invalid Input !! "
    
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
operation = input("Enter the sign of operation you want to perform : ")

print(calculator(num1,num2,operation))
    
     """
# alt + shift + down arrow - replicate line to the next line

# Day 9
# Type Casting in python - convert one data type to another

# Two types of typecasting

# Explicit Conversion
# Implicit Conversion

# Explicit typecasting
""" 
a = 1
b = 2
print(a+b)
print(int(a) + int(b))


# Implicit Typecasting

c = 1.9 

d = 8

print(c+d) """

# taking user input in python

""" 
a = input("Enter your name: ")
print("My name is ",a)
 """

""" 
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

print(x + y) """

""" name = "Abhinav"
friend = "Rohan"

apple = '''He said,
Hi Abhinav
hey I am good
"I want to eat an apple'''

anotherFriend = 'Akash'

print("Hello, " + name)

# muti line string - triple single or triple double quotes

print(name[0])
print(name[1])
print(name[2])

print("Let's use a loop \n")

for character in apple:
    print(character)
 """

# strings slicing and operations on string
""" 
names = "Abhinav,Suman"
print(names[0:6])
print(len(names))

fruit = "Mango"
len1 = len(fruit)
print("Mango is a",len1,"letter word")

print(fruit[0:3])

print(fruit[-1:len(fruit)-3])

print(fruit[-3:-1]) """

# Quick quiz

""" nm = "Abhinav"
print(nm[-4:-2]) """

# String Methods

# Strings are immutable
""" 
a = "!!! AbhinavSUMAN12345 !!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.lstrip("!"))
print(a.strip("!"))
print(a.replace("Abhinav","John"))

print(a.split(" ")) # convert string to list

blogHeading = "introduction to python"
print(blogHeading.capitalize())

str1 = "Welcome to the console"
print(len(str1))
print(len(str1.center(50)))

print(a.count("Abhinav"))

str1 = "Welcome to the Console !!"

print(str1.endswith("!!"))
print(str1.endswith("to",4,10))

str1  = "He's name is Dan . He is an honest man !!"

print(str1.find('ishh')) # gives -1 if not found
# print(str1.index("ishh")) # gives an error if not found

str1 = "Welcome to The Console !!"
print(str1.isalnum())

print(str1.isalpha())

print(str1.islower())

# isprintable - returns True all characters are printables - \n is not printable

str1 = "We wish you a merry christmas !!! \n"
print(str1.isprintable())

# is title - returns True if first character of each letter is Capital
str1 = "World health organization !!"

print(str1.istitle())


# is space - returns true if it has space

str1 = "                 "
print(str1.isspace())


str2 = "   "

print(str2.isspace())

str1 = "Python is an interpreted language !!"
print(str1.startswith("Abhi"))


# swapcase - swap  upper to lower case and vice versa for each character
str1 = "Python is an interpreted language !!"
print(str1.swapcase())

# title - convert first letter of each word to Capital

print(str1.title())

 """

## if - else statement

""" 
a = int(input("Enter your age :"))
print("Your age is :", a)

if (a>18):
    print("You can drive !!")
else:
    print("You cannot drive!!")

 """

# if elif statement

""" applePrice = 20
budget = 200


if budget - applePrice > 50 :
    print("Alexa , add 1 kg apples to the cart !")


elif (budget - applePrice > 70):
    print("It's okay you can buy it !!")

else:
    print("Alexa, do not add Apples to the cart") """


# if elif statement

""" 
num = int(input("Enter the value of num : "))

if num < 0  :
    print(f"{num} is negative !!")


elif num == 0 :
    print(f"{num} is zero !!")

elif num == 999 :
    print(f"{num} is special !!")

else:
    print(f"{num} is positive !!") 

print("I am happy now !!") """



# nested if-else

""" 
num = int(input("Enter the value of num : "))

if num < 0  :
    print(f"{num} is negative !!")

elif num > 0:
    if num <=10:
        print("{num} is between 1-10")
    
    elif num >10 and num <= 20 :
        print(f"{num} is between 11-20 !!")

    else: 
        print(f"{num} is greater than 20 !!")

else:
    print(f"{num} is zero !!") 

print("I am happy now !!") """


# Exercise 2 -- Print Good Morning/Afternoon/Evening/Night Based on Time
""" 
import time
timestamp = time.strftime('%H:%M:%S')

if int(time.strftime('%H')) > 0 and  int(time.strftime('%H'))  <12:
    print(f"Good Morning !! The time is {timestamp}")

elif int(time.strftime('%H')) >=12 and  int(time.strftime('%H')) <=15:
    print(f"Good Afternoon !! The time is {timestamp}")

elif int(time.strftime('%H')) >=4 and  int(time.strftime('%H')) <=19:
    print(f"Good Evening !! The time is {timestamp}" )

else:
    print(f"Good night !! The time is {timestamp} ")

 """


# Match- Case Statement

""" import os
os.system("python --version") """

## match-case -- supported in version 3.10 or later

""" x = int(input("Enter the value of x : "))

match x:

    case 0:
        print("x is zero !!")

    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")

    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)
        """


# for loop in python

""" colors = ["Red","Blue","Orange","Yellow"]

for color in colors:
    print(color) """

""" for k in range(5):
    print(k)

for i in range(1,9):
    print(i) """
""" 
for i in range(1,12,3):
    print(i) """


# while loop

""" i = 0
while(i<3):
    print(i)
    i+=1

print("Done with the loop") """

""" i = int(input("Enter the number : "))

while i <= 38:
    i = int(input("Enter the number : "))
    print(i)

print("Done with loop !!")
 """


""" count = 5


while(count > 0):
    print(count)
    count-=1

 """

# while - else loop

# once the while condition becommes false while it will go inside else

""" count = 5

while count>0:
    print(count)
    count-=1

else:
    print("I am inside while loop") """


# for - else loop

# once the for condition becommes false while it will go inside else


""" for i in range(5):
    print("5")

else:
    print("not 5") """


# do while - runs loops at least one time irrespective of condition is true or not
""" 
do {
    # loop body
}
while(condition); """



""" number = 0
while True:
    print(number)
    number+=1
    if number == 10:
        break """


# break and continue

""" for i in range(12):
    print("5 X",i,"=",5*i)

    if i == 10:
        break

print("Exits from the loop !!") """


# continue - everything above will execute above execute statement
""" 
for i in range(12):
    

    if i == 10:
        print("Skips the iteration !!")
        continue


    print("5 X",i,"=",5*i)

print("Exits from the loop !!") """

# simulating do while loop in python

""" 
i=0
while True:
    print(i)
    i+=1
    if(i%100 == 0):
        break
 """


## functions in python - 
# built in and 
# user defined python

# to avoid repeatabilty of code
# make it modular
# make it more cleaner
""" 

def calculategmean(a,b):
    mean = (a*b)/(a+b)
    return mean
a = 6
b = 8

print(calculategmean(a,b))


def isGreater(a,b):
    if a > b:
        print("First number id greater")
    
    else:
        print("Second number is greater")


# pass function - to leave a function body blank

isGreater(5,10)

def isLesser(a,b):
    pass
 """

# Day 21

# function arguments

# default args
# variable args
# variable length args
# required args - keyword  arguments , kwargs



# variable args

""" def average(a,b):
    print("The average is", (a+b)/2)

average(4,6) """

# default args # take default args if not provided
# no order is required as it is provided explicity

""" def average(a,c=4,b=9):
    print("The average is", (a+b+c)/2)

average(4) """


# variable length args

""" def average(*numbers):
    # take list of numbers as tuples
    print(*numbers)
    sum = 0
    for i in numbers:
        sum +=i
    print("Average is",sum/len(numbers))

average(5,6,7,8,9,10) """

## the list elements can be unpacked using this
""" 
def average(*numbers):
    # unpacks list of numbers as tuples
    print(type(numbers))
    print(numbers)
    sum = 0
    for i in numbers:
        sum +=i
    print("Average is",sum/len(numbers))

numbers_list = [5, 6, 7, 8, 9, 10]

average(*numbers_list)
 """

# unpack dict elements - kwargs **

""" 
def name(**name):
    # to take dict elements
    print(name)
    print(type(name))
    print("Hello",name["fname"],name["mname"],name["lname"])


name(mname="Abhinav",lname="Suman",fname="Mr") """

""" 
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

details_dict = {
    'name':'Abhinav',
    'age':'28',
    'city':'patna',
    'profession':'data engineer' 
}

print_details(**details_dict) """


# Lists - ordered collection of items of different data types
# they are changeable - mutable

""" marks = [3,5,6]
print(marks)
print(type)

print(marks[2])

print(marks[0])


unique = [1,2.4,"Abhinav",True]
print(unique[2])


# list index

marks = [3,5,6,"Harry",True]

print(marks[-3])

# IN operator - list and strings

if  7 in marks:
    print("yes")
else:
    print("no")



if "a" in "marks":
    print("yes")
else:
    print("No")


marks = [3,5,6,"Harry",True,55,33,22,11,666,7,3]
print(marks[1:-1])
print(marks[1:8:3])
 """
# convert negative index to positive

# negative index + length(list)
""" 
def convert_negative_index_to_positive(negative_index, length):
    if negative_index < 0:
        return negative_index + length
    return negative_index

# List example
my_list = [10, 20, 30, 40, 50]
length = len(my_list)


# Converting negative indexes
negative_index = -2
positive_index = convert_negative_index_to_positive(negative_index, length)

print(f"Negative index {negative_index} is equivalent to positive index {positive_index}")
print(f"Element at negative index {negative_index}: {my_list[negative_index]}")
print(f"Element at positive index {positive_index}: {my_list[positive_index]}")
 """

## List Comprehension
""" 
squares = [x**2 for x in range(10)]
print(squares)

evens =  [x for x in range(10) if x%2==0]
print(evens)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

flattened = [elem for row in matrix for elem in row]
print(flattened)

filtered = [x for x in range(10) if x %2 ==0 if x >4]
print(filtered)

categorized = ['small' if x < 3 else 'medium' if x < 7 else 'large' if x<10 else 'extra large' for x in range(15) ]
print(categorized)

def is_prime(n):
    if n<=1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True


primes = [x for x in range(10) if is_prime(x)]
print(primes)

pairs = [(i,j) for i in range(3) for j in range(3) if i!=j]
print(pairs)

list1 = [1,2,3]
list2 = [4,5,6]
sum = [x+y for x,y in zip(list1,list2)]
print(sum)

my_dict = {'a':1, 'b':2,'c':3}
keys = [key for key,value in my_dict.items() if value > 1]
print(keys) """

# set comprehension
""" 
squares = {x**2 for x in range(10)}

print(squares)

evens = {x for x in range(10) if x %2 == 0}
print(evens)


modified = {x**2 if x %2 == 0 else x for x in range(10)}
print(modified)

squares = {x:x**2 for x in range(10)}
print(squares)

evens = {x:x**2 for x in range(10) if x %2==0}
print(evens)

modified = {x:(x**2 if x%2==0 else -1) for x in range(10)}
print(modified)

nested_dict = {(i,j):i+j for i in range(3) for j in range(3)}
print(nested_dict)


def is_prime(n):
    if n<=1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
        
    return True

primes = {x for x in range(20) if is_prime(x)}
print(primes)

primes_dict = {x:is_prime(x) for x in range(20)}
print(primes_dict)

keys =  [ 'a','b','c']
values = [1,2,3]
combined_values = {k:v for k,v in zip(keys,values)}
print(combined_values)
 """

""" lst = [i * i for i in range(4) if i%2==0]
print(lst) """

# l =  [11,45,2,4,6]
# print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(45))
# print(l)

# insert method

# l.insert(1,[2,3])
# print(l)


""" import copy

# List with nested lists
l = [11, 45, [2, 4], 6]

# Shallow copy
m = copy.copy(l)
m[2][0] = 12

print("Original:", l)
print("Shallow Copy:", m)

# Reset the original list
l = [11, 45, [2, 4], 6]

# Deep copy
m = copy.deepcopy(l)
m[2][0] = 12

print("Original:", l)
print("Deepcopy:", m)
 """
""" 
l = [11, 45, [2, 4], 6]
m = [900,1000,1100]


# extend unpacks the list element and add to 
l.extend(m)
print(l)


l = [11, 45, [2, 4], 6]
m = [900,1000,1100]
# append
# add a list like a list to other list

l.append(m)
print(l) """

# concat list elements
# works like extends - inpacks and add to the list

""" 
l = [11, 45, [2, 4], 6]
m = [900,1000,1100]

k = l+m
print(k)
 """

# tuple introduction
# ordered collection of items
# tuples are immutable
# used when we don't want a list to be changed

"""
empty_tuple = ()
print(empty_tuple)

tup = {1,5,6}
print(type(tup),tup)

tup = (1,) #  way of creatng tuple
print(type(tup),tup)

# creating tuple from list

tuple_from_list = ([1,2,4,6])
print(tuple_from_list)

# gives error if you try to change some element
 
tup = (1,2,76,342,32)
tup[0] = 90
print(type(tup),tup)
 """
""" 
# Unpacking elements of a tuple

t = (1,2,3)
a,b,c = t
print(a,b,c)

# Unpacking with *
t = (1,2,3,4,5)
a,*b,c = t
print(a,b,c)

# tuple methods
sample_tuple = (1, 2, 2, 3, 4, 4, 4, 5)


print(sample_tuple.count(4))

print(sample_tuple.index(4)
)

# concatenation of tuple

tuple1 = (1,2,3)
tuple2 = (4,5,6)

concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)


# Repetition

repeated_tuple = tuple1*3
print(repeated_tuple)

# Check if an element exists in the tuple


sample_tuple = (1, 2, 3, 4, 5)



print(3 in sample_tuple)
print(6 in sample_tuple)

# Get the length of the tuple

sample_tuple = (1, 2, 3, 4, 5)
print(len(sample_tuple))


# Accessing elements in nested tuples

nested_tuple = ((1,2),(3,4),(5,6))
print(nested_tuple)
print(nested_tuple[0][0])

# Converting a list to a tuple

sample_list = [1,2,3,4,5,6]
converted_tuple = tuple(sample_list)
print(converted_tuple)

# Converting a string to a tuple


sample_string = "hello"
string_to_tuple = tuple(sample_string)
print(string_to_tuple) """

# manipulating tuples
# change to list , do modifications , change back to list

""" countries = {"Spain","Italy","India","England","Germany"}

temp = list(countries)
temp.append("Russia")
temp.pop(3)
print(temp)
temp[2] = 'Finland'
countries = tuple(temp)
print(countries) """

# concatenate tuple 

""" countries1 = ("Pakistan","Afganistan","Bangladesh","Bangladesh","Srilanka")

countries2 = ("Vietnam","India","China")

southEastAsia  = countries1 + countries2

print(southEastAsia)
 """
# tuple methods

""" sample_tuple = (1, 2, 2, 3, 4, 4, 4, 5)
print(sample_tuple.count(4))
print(sample_tuple.index(3,3,7))
print(len(sample_tuple)) """

""" import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if hour >=0 and hour <12:
    print("Good Morning Sir !!")

elif hour >= 12 and  hour <17:
    print("Good Afternoon Sir !!")

elif hour >= 17 and  hour < 0:
    print("Good Night Sir !!")    
 """

# Create a program capable of displaying questions to the user like KBC.
# Use list  data type to store the questions and their answers
# display the final amount the person is taking home after playing the game

""" 


questions = [
    ("What is the capital of India?", ["Mumbai", "Delhi", "Kolkata", "Chennai"], 2),
    ("Who wrote the Indian National Anthem?", ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Subhash Chandra Bose", "Mahatma Gandhi"], 1),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 2),
    ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2),
    ("Who is known as the Father of the Indian Nation?", ["Jawaharlal Nehru", "Mahatma Gandhi", "Bhagat Singh", "Subhash Chandra Bose"], 2),
    ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "NaCl"], 1),
    ("Which country is known as the Land of the Rising Sun?", ["China", "India", "Australia", "Japan"], 4),
    ("What is the smallest prime number?", ["0", "1", "2", "3"], 3),
    ("Which language is used for web apps?", ["PHP", "Python", "JavaScript", "All"], 4),
    ("Which company is known for the iPhone?", ["Microsoft", "Google", "Apple", "Samsung"], 3)
]

def display_question(question,options):
    print("\n",question)
    for i , option in enumerate(options):
        print(f"{i+1}.{option}")


def get_user_answer():
    while True:
        try:
            answer = int(input("Enter the option number {1-4} : "))
            if answer in range(1,5):
                return answer
            
            else:
                print("Please enter a valid option number between 1 and 4.")
            
        except ValueError:
            print("Invalid input,Please enter a number !!")

def play_kbc(questions):
    prize_money = 0
    levels = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000]

    for i,(question,options,correct_answer) in enumerate(questions):
        display_question(question,options)
        user_answer = get_user_answer()

        if user_answer == correct_answer:
            prize_money = levels[i]
            print(f"Correct! You have won ₹{prize_money}")
        else:
            print("Incorrect answer. Game over.")
            break

    print(f"\nCongratulations! You are taking home ₹{prize_money}")


# Start the game
play_kbc(questions) """


# old python formatting
""" 
letters = "Hey my name is {1} and  am from {0}"

country = "India"
name = "Abhinav"

print(letters.format(country,name))

# f - string

print(letters.format(country,name))
print(f"Hey my name is {name} and I am from {country}")

txt = "For only {price:.2f} dollars"
print(txt.format(price=49.9999))

# if we do  want placeholders inside curly braces

print(f"Hey my name is {{name}} and I am from {{country}}")
 """


# docstrings =-> string literals that appear after the definition of a function,method,class or module
# these are comments to understand the funcctionality of the program

""" import math
def square(s):
    '''Takes in a number n,returns square of n'''
    print(s**2)

square(5)
print(square.__doc__) # print a doc string of inbulit function
print(abs.__doc__)
help(math.sqrt.__doc__)

import this # piem by tim peters """

# Day 30

# Recursion

# function calling itself 

# factorial (5) = 5*4*3*2*1
# factorial (0) = 1

# factorial (n) - n* factorial(n-1)

""" def factorial(n):
    if n == 0 or n==1:
        return 1
    
    else:
        return n * factorial(n-1)
    
print(factorial(5)) """

# 5 * factorial(4)
# 5 * 4 *  factorial(3)
# 5 * 4 * 3 factorial(2)
# 5 * 4 * 3 * 2  factorial(1)
# 5 * 4 * 2* 1 = 120

# fibonacci series 
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f (0)
# f(n) = f(n-1) + f(n-2)

# without recursion

""" def fibonacci_iterative(n):
    fib_series = []
    a,b = 0,1
    for i in range(n):
        fib_series.append(a)
        a,b = b,a+b

    return a

print(fibonacci_iterative(4))
 """
# with 
# time complexity - O(2^n)
# space complexity - O(n)
""" 
def fibonnaci_recursive(n):
    if n<=0:
        return 0
    
    elif n ==1:
        return 1
    
    return fibonnaci_recursive(n-1) + fibonnaci_recursive(n-2)


def generate_fibonacci_series(n):
    return [fibonnaci_recursive(i) for i in range(n)]

n =5

print(f"Fibonacci series (recursive):{generate_fibonacci_series(n)}") """


# Sets in python

# unique unordered collection of items - no duplicate elements
# sets are immutable
# no order is maintaned

""" 
s = {2,4,2,6}
print(s)
print(type(s))

info = {"Carla",19,False,5.9,19}
print(info)

# to create empty set

abhinav = set()
print(type(abhinav))

# loop over set

for value in info:
    print(value) """

## day 32

# set operations
""" 
s1 = {1,2,5,6}
s2 = {3,6,7}

# union 

print(s1.union(s2))
print(s1|s2)

# intersection
print(s1.intersection(s2))
print(s1&s2)

# set difference
print(s1.difference(s2))
print(s1-s2)

# symmetric difference in set - either in set a or set b but not both
print(s1.symmetric_difference(s2))

# update one set
s1.update(s2)
print(s1,s2)

# union vs union update - update set with union result

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}

# cities.update(cities2) # for union - update cities with union result
# print(cities)

# for intersection  - update cities with intersection result
# cities.intersection_update(cities2) 
# print(cities)

# difference vs difference update - update set with set difference

# cities.difference_update(cities2)
# print(cities)

# disjoint sets - two sets are disjoint if they don't have elements in common

print(cities.isdisjoint(cities2))
# false - since they have elements in common

# superset - if all elements of b are in a - a is superset of b

print(cities.issuperset(cities2))

# subset - if all elements of a are in b - a is subset of b

print(cities.issubset(cities2))

# other sets  method 

# add

cities.add("Helsinki")
print(cities)

# update - for adding one or more items to sets

cities2={"Munich","Paris","Benningen","Basel"}
cities.update(cities2)
print(cities)

# remove -- raises error if element not present

# cities.remove("d")
# print(cities)

# discard

# discard -- does not give error if element not present

cities.discard("Helsinki")
print(cities)

# pop method - removes element, by default  any random element from set

cities.pop()
print(cities)

# del method - deleting entire set

# del cities
# print(cities) # will give error as cities is not present

# clear - set is not deleted but all items are present

# print(cities.clear())

# in operator

# if 'Madrid' in cities:
#     print("yes")


 """

# Day 33

# Dictionaries in python
# dict is ordered in python 3.7 onwards
# ordered collection of items
# key-value-pairs  seperated by comma, enclosed with {}
""" 
info = {
    344: "Abhinav",
    505:"Shubham",
    678:"Zakir",
    567:"Akash"
}

# access element of dict - gives error if element not present
print(info[344])


# access element of dict - does not gives error - gives None if element is not present

print(info.get('eligible'))

# get all keys

print(info.keys())

# another way
for key in info.keys():
    print(f"value is {info[key]}")

# get all values

print(info.values())

# print key - values using - items --  type - dict items
print(info.items())
print(type(info.items()))

# iterating over key and value in dict using -- dict.items()

for key,value in info.items():
    print(key,value) """

# day 34

# dict methods in python

# dict is ordered in python 3.7 onwards
""" 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# adding element to dict


thisdict['color'] = "red"
print(thisdict)

# update - update the existing value in dict or it adds if it is not present

ep1 = {122:45,123:89,567:89,670:69}

ep2 = {222:67,566:90}

ep1.update(ep2)

print(ep1)

# clear a dict

# ep1.clear()


# create empty dict
emp_dict = {}

#pop - remove element from dict for key given
ep1.pop(122)
print(ep1)

#pop item - remove last element from the list

ep1.popitem()
print(ep1)


# delete item from a dict for a given key , if key is not provided delete entire dict

del ep1[123]
print(ep1)

# del ep1
# print(ep1)

 """

# day 35 - for else

# once for loop executes successfully it goes to the else loop just like while-else


# if broken using break it will not go to else
""" 
for i in []:
    if i==0:
        print("Hello")
else:
    print("not required")


# if broken using break it will not go to else

for i in range(6):
    print(i)
    if i == 4:
        break

else:
    print("Sorry No !!")


# same for while-else

#once while loop executes successfully it goes to the else loop


# if broken using break it will not go to else

i = 0
while i < 7:
    print(i)
    i+=1
    if i == 4:
        break

else:
    print('else block !') """

# Day 36

# Exception handling in python

# Exception prevent system crashing or terminating of program abruptly

# built in exceptions 

# except Exception as e -  handles all error

# except - handles all error

# except valueError - handles specific error



#try except block
""" 
try:
    
    a = input("Enter the number : ")
    arr = [6,3]
    print(arr[int(a)])
    print("Multiplication table of {a} is")

    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
# handling specific error
except ValueError as e :
    print(" \n Sorry Invalid input !!  Error : ",e)
except IndexError as e:
    print("Index is out of range !! Error : ",e)

print("Some imp lines of code")
print("End of program") """


# day 37 : 

# Finally keyword in Python

# whether goes inside try or except - finally -> it is always executed

""" try : 
    l = [1,3,5,7]
    i = int(input("Enter the index : "))
    print(l[i])

except:
    print("Some error occured !!")

finally:
    print("I am always executed !!") """

## day 37
""" 
def func1():
    try : 
        l = [1,3,5,7]
        i = int(input("Enter the index : "))
        print(l[i])
        return 0

    except:
        print("Some error occured !!")
        return 1
    
    #  it is always executed - even you are returning try or except - finally will run

    finally:
        print("I am always executed !!")

    # this code will not run - it should be put in finally
    print("I am always executed !!")

x = func1()
print(x) """

# day 38

# custom error raising

# to handle the error at any time
# ex - input is not in correct format
# ex - data is not present in the server

""" 
a = input("Enter any value between 5 and 9 (Enter q or quit to quit ) : ")

def myfunc():
    if a == 'quit' or a == 'q':
        print("You have successfully quitted the program !!!")
        exit()
    elif int(a) < 5 or int(a) > 9:
        raise ValueError("Value should be between 5 and 9")
    else:
        print(a)

myfunc() """

## day 39
""" 
questions = [
    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],

    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],

    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],

    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],
    
    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],

    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],

    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],

    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],

    ["Which language was used to create FB","Python","French","Javascript","Php","None",4],

    ["Which language was used to create FB","Python","French","Javascript","Php","None",4]






]


levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

i = 0

for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f" a.{question[1]}    a.{question[2]}")
    print(f" c.{question[3]}    d.{question[4]}")

    reply = int(input("Enter your answer {1-4} : "))

    if(reply == question[-1]):
        print(f"Correct answer,you have won Rs : {levels[i]}")

    if i == 4:
        money = 10000
    elif i == 9:
        money = 320000
    elif i == 14:
        money = 10000000
        
    elif reply != question[-1]:
        print("Wrong Answer !!")
        break

if i == len(levels)-1:
    print("\n")
    print("***********************************")
    print("you are the winner of KBC 2024 !!!")
    print('your take home winning amount is : ',levels[i])

else:
    print("\n")
    print("***********************************")
    print("Unfortunately !!! your journey ends here !")
    print('your take home winning amount is : ',levels[i-1])    
 """

# day 41

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
""" 
import random
import string


def encoded_message(message):
    if len(message)>3:
        first_letter = message[0]
        encrpyted_message = message[1:] + first_letter

        characters = string.ascii_letters + string.digits  # Combination of uppercase, lowercase, and digits
        first_three_letters= ''.join(random.choice(characters) for _ in range(3))
        last_three_letters = ''.join(random.choice(characters) for _ in range(3))

        return (first_three_letters + encrpyted_message + last_three_letters)

    else:
        encrpyted_message = message[::-1]
        return (encrpyted_message)
    

def decoded_message(message):
    print(message)
    if len(message)<3:
        decrypted_message = message[::-1]
        return decrypted_message

    else:
        print(message)
        return message[-4]+message[3:-4]

    
message = input("Enter your message to be encrypted !! : ")

encrypted_message = encoded_message(message)

print(decoded_message(encrypted_message)) """

""" 
import random
import string

def encoded_message(message, num_random_chars):
    if len(message) > num_random_chars:
        first_letter = message[0]
        encrypted_message = message[1:] + first_letter

        characters = string.ascii_letters + string.digits  # Combination of uppercase, lowercase, and digits
        first_random_chars = ''.join(random.choice(characters) for _ in range(num_random_chars))
        last_random_chars = ''.join(random.choice(characters) for _ in range(num_random_chars))

        return first_random_chars + encrypted_message + last_random_chars

    else:
        encrypted_message = message[::-1]
        return encrypted_message
    

def decoded_message(message, num_random_chars=3):
    if len(message) <= 2 * num_random_chars:
        decrypted_message = message[::-1]
        return decrypted_message

    else:
        decrypted_message = message[num_random_chars:-num_random_chars]
        return decrypted_message[-1] + decrypted_message[:-1]

    
# Example usage
message = input("Enter your message to be encrypted !! : ")
num_random_chars = 3  # You can change this value to be more dynamic

encrypted_message = encoded_message(message, num_random_chars)
print("Encrypted message:", encrypted_message)

decrypted_message = decoded_message(encrypted_message, num_random_chars)
print("Decrypted message:", decrypted_message)
 """

# day 41

# short hand if else

