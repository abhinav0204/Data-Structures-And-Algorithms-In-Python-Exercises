### sum of n natural numbers

""" n = int(input("Enter n: "))

sum = n*(n+1)//2

print("sum is ",+sum) """

# count number of digits in a number
""" 
x = int(input(" Enter a number x : "))

res = 0

while x>0:
    x = x//10
    res+=1

print("Count of digits in the number is", + res) """

## palindrome number

""" def isPal(number):
    rev = 0
    temp = number

    while temp != 0 :
        last_digit = temp % 10
        rev = rev*10+ last_digit
        temp = temp //10
    
    return number == rev


if __name__ == '__main__':
    number = int(input("Enter a number : "))
    print(isPal(number)) """


# factorial of a number - iterative approach
""" 
def fact(n):
    res = 1
    for i in range(2,n+1):
        res = res * i
    
    return res

if __name__ == '__main__':
    num = int(input("Enter a number : "))
    print(fact(num))
 """

# factorial of a number - recursive appraoch

""" def fact(n):

    # base case
    if n == 0 :
        return 1
    
    return n * fact(n-1)

if __name__ == '__main__':

    num = int(input("Enter a number : "))
    print(fact(num))
 """

## trailing zeroes in a number

## fact value in this approach is super large
## overflow of value in other languages

""" def countZeroes(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    res = 0
    while(fact%10 == 0):
        res+=1
        fact = fact// 10
    return res

if __name__ == '__main__':
    num = int(input("Enter a number : "))
    print(countZeroes(num)) """


## trailing zeroes in a number

## count of two and five in prime factorization of the number (2 * 5 = 10)
## since number of 5's are less than 2 we can count only number of 5

""" def countZeroes(n):
    res = 0
    i = 5
    while(i<=n):
        res = res + n//i
        i = i * 5

    return res

if __name__ == '__main__':
    num = int(input("Enter a number : "))
    print(countZeroes(num))

 """

 ## gcd of two numbers -

 ## 1) basic approach

""" def gcd(num1,num2):

    result = min(num1,num2)

    while result:
        if num1 % result == 0 and num2 % result == 0 :
            break
        result = result - 1

    return result


if __name__ == '__main__':
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(f"GCD of {num1} and {num2} is {gcd(num1,num2)}")


 """

 ## approach 2 - euclidean approach
""" 
def gcd(num1,num2):

    while(num1 != num2):
        if (num1 > num2):
            num1 = num1 -  num2

        else:
            num2 = num2 - num1

    return num1
 
if __name__ == '__main__':
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(f"GCD of {num1} and {num2} is {gcd(num1,num2)}") """

 ## approach 2 - euclidean approach - optimised

""" def gcd(num1,num2):
    
    if num2 == 0:
        return num1
    return gcd(num2,num1%num2)




if __name__ == '__main__':
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(f"GCD of {num1} and {num2} is {gcd(num1,num2)}")
 """

## lcm of two numbers -

# naive approach

""" def lcm(num1,num2):

    res = max(num1,num2)

    while True:

        if res % num1 == 0  and res % num2 == 0:
            return res
        res+=1

    return res
        

if __name__ == '__main__':
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(f"LCM of {num1} and {num2} is {lcm(num1,num2)}") """


# optimised approach - a * b = gcd(a,b) * lcm(a,b)

## lcm of two numbers -
""" 
def gcd(num1,num2):

    if num2 == 0:
        return num1
    
    return gcd(num2,num1%num2)

def lcm(num1,num2):
    return num1*num2 //gcd(num1,num2)

if __name__ == '__main__':
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(f"LCM of {num1} and {num2} is {lcm(num1,num2)}") """


## Check for prime number 
# basic approach

""" def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2,n):
        if n% i == 0:
            return False
    
    return True

if __name__ == '__main__':
    n = int(input("Enter a number to check : "))
    if isPrime(n):
        print(f"{n} is a prime number !!")
    else:
        print(f"{n} is not a prime number !! ")
 """

## optimised approach -- checking if divisor pair is less than n  (i*i) <= n

""" def isPrime(n):
    if n == 1:
        return False
    
    i = 2

    while(i*i<=n):
        if n%i == 0:
            return False
        i+=1

    return True


if __name__ == '__main__':
    n = int(input("Enter a number to check : "))
    if isPrime(n):
        print(f"{n} is a prime number !!")
    else:
        print(f"{n} is not a prime number !! ") """

##  super optimised approach 

""" def isPrime(n):

    if n == 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n%2 == 0  or n% 3 == 0:
        return False
    
    i = 5
    
    while( i * i <= n):
        if  n% i == 0 or n% (i+2) == 0 :
            return False
        
        i+=6

    return True

if __name__ == '__main__':
    n = int(input("Enter a number to check : "))
    if isPrime(n):
        print(f"{n} is a prime number !!")
    else:
        print(f"{n} is not a prime number !! ") """


## prime Factorisation

""" def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def primeFactor(n):
    for i in range(2,n+1):
        if isPrime(i):
            x = i
            while n%x == 0:
                print(i,end = ' ')
                x = x*i



n = int(input("Enter a number : "))
primeFactor(n) """

## prime Factorisation - optimsed

""" import math

def primeFactors(n):

    while n%2 == 0:
        print(2)
        n = n//2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0 :
            print(i,end=' ')
            n = n//i

    if n > 2:
        print(n)


n = int(input("Enter a number : "))
primeFactors(n) 
 """

## all divisors of a number

## naive approach o(n)

""" def Divisors(n):
    for i in range(1,n+1):
        if n% i == 0:
            print(i,end=' ')



n = int(input("Enter a number : "))
print(f"The divisors of n are ",end =' ')
Divisors(n) """

## optimised approach -  sqrt(n) --  but not in order


""" def Divisors(n):
    i=1
    while(i*i<=n):
        if n % i == 0 :
            print(i,end=' ')
        
            if i != n/i :
                print(n//i,end = ' ')
        i+=1



n = int(input("Enter a number : "))
print(f"The divisors of n are ",end =' ')
Divisors(n)
 """

##  more optimised approach -- sqrt(n) -- in sorted order

""" 
def Divisors(n):
    i = 1
    while(i*i<n):
        if n%i == 0:
            print(i,end =' ')  ## divisors from 1 to sqrt(n)
        i+=1

    while(i>=1):
        if n % i ==0:
            print(n//i,end=' ') ## divisors from  sqrt(n) to 1
        i-=1

n = int(input("Enter a number : "))
print(f"The divisors of n are ",end =' ')
Divisors(n)

 """

##  prime numbers 1 to n - optimised approach -  (n*sqrt(n))

""" def isPrime(n):

    if n == 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n% 2 == 0 or n% 3 == 0:
        return False
    
    i = 5
    while(i*i <= n):

        if n%i == 0 or n% (i+2) == 0 :
            return False
        
        i+=6

    return True


def primeCheck(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(i,end=' ')


if __name__ == '__main__':
    n = int(input("Enter a number : "))
    primeCheck(n) """

## sieve of eartosthenes - prime numbers - 1 to n - o(n loglog n)

""" 
def sieve(n):

    if n<= 1:
        return False
    
    isPrime = [True] * (n+1)

    i = 2

    while( i * i <= n):
        if isPrime[i]:
            for j in range(2*i, n+1,i):
                isPrime[j] = False

        i+=1

    for i in range(2,n+1):
        if isPrime[i]:
            print(i,end=' ')


if __name__ == '__main__':
    n = int(input("Enter a number : "))
    sieve(n)
 """

## sieve of eartosthenes - optimized - prime numbers - 1 to n - o(n loglog n)


""" def sieve(n):

    if n<=1:
        return 
    
    isPrime = [True] * (n+1)
    
    i = 2
    while i*i <= n:
        if(isPrime[i]):
            for j in range(i*i,n+1,i):  ## inly checking the squares of primes
                isPrime[j] = False

        i+=1

    for i in range(2,n+1):
        if isPrime[i]:
            print(i,end=" ")

if __name__ == '__main__':
    n = int(input("Enter a number : "))
    sieve(n) """


# computing power -- power of a number


## naive approach -- 0(n)


""" def powerOfANumber(n,x):

    pow = 1

    for i in range(x):
        pow = pow * n
    return pow


if __name__ == '__main__':
    n = int(input("Enter a number : "))
    x = int(input("Enter the power : "))
    print(powerOfANumber(n,x)) """


##  optimised approach -- recursive approach

""" def PowerOfANumber(n,x):
    if n == 0:
        return 0
    
    if x == 0:
        return 1
    
    temp = PowerOfANumber(n,x//2)

    temp = temp * temp
    
    if (x%2 == 0):
        return temp
    
    else:
        return temp *n



if __name__ == '__main__':
    n = int(input("Enter a number : "))
    x = int(input("Enter the power : "))
    print(PowerOfANumber(n,x)) """

## binary expotentiation approach - O (log(n))
""" 
def PowerOfANumber(n,x,m):
    res = 1
    while x> 0 :
        if x&1:
            res = (res*n)%m
        
        n =(n*n)%m
        x =x>>1
    return res


if __name__ == '__main__':
    n = int(input("Enter a number : "))
    x = int(input("Enter the power : "))
    m = (1e9)+7
    print(PowerOfANumber(n,x,m))
 """