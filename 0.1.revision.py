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
