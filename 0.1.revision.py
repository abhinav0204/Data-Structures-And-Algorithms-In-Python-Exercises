#1. sum of n natural numbers

# 1st approach - O(1)

""" def fun(n):
    return n* (n+1)/2

num = int(input("Enter a number : "))
print(f'The sum of {num} natural numbers is : {fun(num)} ')
 """

# 2nd approach - O(n)

""" 
def fun(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+i
    
    return sum

num = int(input("Enter a number : "))
print(f'The sum of {num} natural numbers is : {fun(num)} ')
 """

# 3rd approach - O(n^2)

""" 
def fun(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum = sum +1

    return sum


num = int(input("Enter a number : "))
print(f'The sum of {num} natural numbers is : {fun(num)} ')
 """

## sum of n natural numbers
""" 
num = int(input("Enter a number : "))
sum = num*(num+1)/2
print(f'The sum of {num} natural numbers is : {sum} ') """



## number is prime or not

# 1st approach - O(n)
""" 
def isPrime(n):

    if n == 1:
        return False
    
    for i in range(2,n):
        if n%i == 0:
            return False
        
    return True

if __name__== '__main__':
    n = int(input("Enter a number : "))
    print("True") if isPrime(n) else print("False")

 """
# another approach - O( sqrt(n))
""" 
def isPrime(n):
    if n == 1:
        return False
    
    i = 2

    while(i* i <=n):
        if n % i == 0:
            return False
        
        i+=1
        
    return True

if __name__== '__main__':
    n = int(input("Enter a number : "))
    print("True") if isPrime(n) else print("False")
 """


# best approach - O( sqrt(n))

""" 
def isPrime(n):

    if n == 1:
        return False
    
    if n ==2 or n ==3:
        return True
    
    if n%2 ==0 or n % 3 == 0:
        return False
    
    i = 5

    while(i*i <=n):
        
        if n % i == 0 or n% (i+2)==0:
            return False
        
        i+=6
    
    return True

if __name__== '__main__':
    n = int(input("Enter a number : "))
    print("True") if isPrime(n) else print("False") """

## prime factorisation
""" 
import math

def isPrime(x):
    i =2
    for i in range(2,x):
        if x % i == 0:
            return False
        
    return True


def printPFactors(n):
    for i in range(2,n+1):
        if isPrime(i):
            x = i
            while n % x == 0:
                print(i,end=' ')
                x = x*i


if __name__== '__main__':
    n = int(input("Enter a number : "))
    printPFactors(n) """


## print Divisors

## Approch 1 - not in sorted order - O( sqrt(n))
""" 
def printDivisors(n):
    i = 1
    while(i * i <= n):
        if n % i == 0:
            print(i,end=' ')
            if ( i != n/i):
                print(n//i,end=' ')
    
        i+=1

if __name__== '__main__':
    n = int(input("Enter a number : "))
    printDivisors(n)    
 """


# Approach 2 -  sorted order - O(sqrt(n))
""" 
def printDivisors(n):
    i = 1
    while(i * i < n):
        if n % i == 0:
            print(i,end=' ')

        i+=1

    while (i >=1):
        if n % i == 0:
            print(n//i,end = ' ')
        
        i-=1
        


if __name__=="__main__":
    n = int(input("Enter a number : "))
    printDivisors(n)

 """


# Sieve of erathosthenes -  Find all prime numbers 1 to N of a given number

# 1st approach

# Time complexity - O (n* sqrt(n))

""" 
def isPrime(n):

    if n == 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while (i * i <= n):
        
        if n% i == 0 or n % (i+2) == 0:
            return False
        
        i+=6

    return True


def printPrimes(n):
    for i in range(2,n+1):

        if isPrime(i):
            print(i,end=' ')



if __name__=='__main__':
    n = int(input("Enter a number : "))
    printPrimes(100) """


# 2nd approach

# Time complexity - O (n* log log n)

# Space complexity - O(1)


""" 
def isPrime(n):

    if n == 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while (i * i <= n):
        
        if n% i == 0 or n % (i+2) == 0:
            return False
        
        i+=6

    return True

def sieve(n):

    if n <= 1:
        return 
    
    isPrime = [True] * (n+1)

    i = 2

    while i <= n:

        if isPrime[i]:
            print(i,end=' ')
            for j in range(i*i,n+1,i):
                isPrime[j] = False

        i+=1

if __name__ == "__main__":
    n = int(input("Enter a number : "))
    sieve(100)


 """

## Computing power

# Time complexity - O(n)

""" def toPower(x,n):

    res = 1
    for i  in range(n):
        res = res * x

    return res


if __name__ == "__main__":
    n,power = map(int,(input("Enter a number and power : ").split(",")))
    result = toPower(n,power)
    print(f"{n} to the power of {power} is {result}")
 """

# Time complexity - O(logn)
# Space complexity - O (logn)
""" 
def toPower(x,n):

    if n == 0:
        return 1
    
    temp = toPower(x,n//2)
    temp = temp * temp

    if (n%2 == 0):
        return temp
    
    else:
        return temp * x
    
if __name__ == '__main__':
    num,pow = map(int, input("Enter the number and the power :").split(","))
    result = toPower(num,pow)
    print(f"{num} to the power of {pow} is {result}")

    
 """

## Computing power
## Iterative power - Iterative Solution

# Time complexity - O(logn)
# Space complexity - O (1)

""" def toPower(x,n):
    res = 1
    while n>0:
        if n % 2 != 0:
            res = res * x

        x = x*x
        n = n//2

    return res

print(toPower(2,5))
 """


## Lists

# Dynamic size
# Allows items of different type


"""
l = [10,20,30,40,50]

print(l)

print(l[3])

print(l[-1])

print(l[-2])

 """
""" 
l = [10,20,30,40,50]

l.append(30)

print(l)

l.insert(1,15)

print(l)

l.extend([60])  # unpacks the list and append it to the list

print(l)

l.append([155,65,778,456,34])  # add elements of the list inside the list

print(l)

print(15 in l)

print(l.count(30))

print(l.index(30)) # if item is not present -- index will give error

print(l.index(30,4,7)) # search 30 from start index - 4 to end index(exclusive) - 6
 """


## list removing elements oprerations

""" 
l = [10,20,30,40,50,60,70,80]

l.remove(20)  # if item is not present remove func gives error

print(l)

print(l.pop( )) # prints removed item using pop function

print(l)

print(l.pop(2)) # pop function takes index

print(l)

del l[1]

print(l)

del l[0:2] # specifying range of indexes with del function

print(l) """

## some more functions
""" 
l = [10,40,20,30]

print(max(l))

print(min(l))

print(sum(l))

l.reverse()

print(l)

l.sort()

print(l) """


## List Advantages

# Random access of elements
# Cache Friendly

## List Disadvantages

# Insertion,Deletion are slow

# Searching is also slow in unsorted array


# Average of a list

# naive approach


""" def average(l):
    sum = 0
    for x in l:
        sum +=x
    n = len(l)
    return sum/n

l = [10,20,30,40]
print(average(l)) """

## less code approach
""" 
def average(l):
    return sum(l)/len(l)


l = [10,20,30,40]
print(average(l)) """

# seperate even or odd
""" 
l = [10,41,30,15,80]

def getEvenOdd(l):
    even = []
    odd = []

    for x in l:
        if x % 2 == 0:
            even.append(x)
        
        else:
             odd.append(x)

    return even,odd

l = [10,12,11,16]

even,odd = getEvenOdd(l)
print(even,odd) """


# Get smaller elements

""" def getSmaller(l,x):
    res = []
    for ele in l:
        if ele < x:
            res.append(ele)
    return res

l = [8,100,20,40,3,7]
x = 10
print(getSmaller(l,x)) """

# Slicing (List, Tuple, String)

""" l = [10,20,30,40,50]

print(l[0:5:2])

print(l[:4])

print(l[2:])

print(l[4:1:-1])

print(l[-1:-6:-1])

print(l[::-1]) """

""" l1 = [10,20,30]
l2 = l1[:]

print(l1 is l2) # False - refers to different object as list are mutable


t1 = (10,20,30)
t2 = t1[:]

print(t1 is t2) # True - refers to same object as tuples are immutable

s1 = "geeks"
s2 = s1[:]

print(t1 is t2) # True - refers to same object as strings are immutable
 """

# list comprehension

""" 
l1 = [x for x in range(11) if x%2 ==0]
print(l1)

l2 = [ x for x in range(11) if x %2 !=0]
print(l2)

even = []
odd = []
even_odd_list = [even.append(x) if x %2 ==0  else odd.append(x) for x in range(11) ]

print(even,odd)

l = [3,6,13,16,10,20,30,40,60,80,100]
smaller_than_x = [e for e in l if e < 20]

print(smaller_than_x) """

""" 
s = "geeksforgeeks"

l1 = [x for x in s if x in "aeiou"]

print(l1)

l2 = ["geeks","ide","courses","gfg"]
l3 = [x for x in l2 if x.startswith("g")]
print(l3)

l4 = [x*2 for x in range(6)]
print(l4)

# set comprehension

l = [10,20,3,4,10,20,7,3]

s1 = {x for x in l if x %2==0}
s2 = {x for x in l if x %2 != 0}

print(s1)
print(s2)

# disctionary comprehension

l1 = [1,3,4,2,5]
d1 = {x:x**3 for x in l1}

print(d1)

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)

l2 = [101,103,102]
l3 = ["gfg","ide","courses"]

d3 = {l2[i]:l3[i] for i in range(len(l2))}
print(d3)

# create dict from two lists - zip method

l2 = [101,103,102]
l3 = ["gfg","ide","courses"]

d3 = dict(zip(l2,l3))
print(d3) """

# dictionary comprehension

# Inventing a dictionary ( key becomes value and value becomes key)
""" 
d1 = {'101':"gfg",103:"pratice","102":"ide"}
d2 = {v:k for  (k,v) in d1.items()}

print(d2) """


# Largest element in a list

""" l = [10,5,20,8]
print(l)

l = [30,30,20]
print(max(l))
 """

# naive approach - O(n^2)

""" def getMax(l):
    for x in l:
        for y in l:
            if y>x:
                break
        else:
            return x
        
    return None

list1 = [10,20,5,50]
print(getMax(list1))


 """

# modified approach - O(n)

""" 
def getMax(l):
    if not l:
        return None
    
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i] > res:
                res = l[i]

        return res

l = [20,10,14,50,30,50,60]  
print(getMax(l))

 """

## second largest element in list

# naive approach - O(n)
# two traversals

""" 
def getMax(l):
    res = l[0]
    for i in range(1,len(l)):
        res = max(res,l[i])
    return res

def getSecMax(l):
    if len(l)<=1:
        return None
    
    larg = getMax(l)
    slarg = None

    for x in l:
        if x!= larg:
            if slarg == None:
                slarg = x

            else:
                slarg = max(slarg,x)

    return slarg


l = [5,20,12,10,20,10,12]
print(getSecMax(l)) """


# advanced approach - O(n)
""" 
def getSecMax(l):
    if len(l) <=1:
        return None
    
    larg = l[0]
    slarg = None

    for i in range(1,len(l)):
        if i > larg:
            larg = l[i]
            slarg = larg

        elif i != larg:
            if slarg == None or l[i] > slarg:
                slarg = l[i]

    return slarg

l = [5,20,12,10,20,10,12]
print(getSecMax(l)) """

# Check if list is sorted or not

#Method 1 ( Traverse using loops)
""" 
def isSorted(l):
    i=0
    while i < len(l)-1:
        if l[i]  >  l[i+1]:
            return False
        
        i+=1

    return True

l = [5,20,12,10,20,10,12]
print(isSorted(l))
 """
""" 
# Method 2 - Sorted function

def isSorted(l):
    return l == sorted(l)

l = [5,20,12,10,20,10,12]
print(isSorted(l)) """

## Reverse a list 

# library methods

""" l = [10,20,30]

l.reverse()
print(l)

l = [10,20,30]

new_list = list(reversed(l))
print(new_list)

l = [10,20,30]

new_list = l[::-1]
print(new_list) """


""" 
def reverse_list(l):
    start = 0
    end = len(l)-1

    while(start < end):
        l[start],l[end] = l[end],l[start]
        start+=1
        end-=1

    return l

l = [5,20,12,10,20,10,12]
print(reverse_list(l)) 

 """

## Remove duplicates from a sorted array

# naive approach
# time complexity - O (n)
# space complexity - O (n)
""" 
def removedup(arr,n):
    temp = [0] * n
    temp[0] = arr[0]
    res = 1

    for i in range(1,n):
        if temp[res-1] != arr[i]:
            temp[res] = arr[i]
            res+=1

    for i in range(0,res):
        arr[i]= temp[i]

    return res

l = [10,20,20,30,30,30,30]
print(removedup(l,len(l))) 

 """


# naive approach
# time complexity - O (n)
# space complexity - O (n)


""" 
def removedup(arr,n):
    res=1
    for i in range(1,n):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res+=1

    return res            

l = [10,20,20,30,30,30,30]
print(removedup(l,len(l))) 
 """

# Left rotate a  list by one

# using direct methods
""" 
l = [10,20,30,40]
l = l[1:] + l[0:1]
print(l)


l = [10,20,30,40]
l.append(l.pop(0))
print(l) """

# Custom function


""" 
def rotateByOne(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    
    l[n-1] = x
    return l

l = [10,20,30,40]
print(rotateByOne(l)) """