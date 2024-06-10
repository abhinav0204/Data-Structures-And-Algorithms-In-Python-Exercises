# sum of all natural numbera

""" n = int(input("Enter a number :"))
sum = n*(n+1)/2
print("Sum is "+ str(sum)) """

# count number of digits 
""" 
def countdigits(n):
    count=0
    while(n>0):
        n =n//10
        count+=1
    return count


n = int(input("Enter a number: "))
print(countdigits(n)) """

# palindrome number

""" def isPal(n):
    rev = 0
    temp = n
    while(temp != 0):
        ld = temp%10
        rev = rev*10 + ld
        temp = temp//10
    
    return rev == n

if __name__ == '__main__':
    number = 4553
    print(isPal(number)) """

# factorial of a number 

# Approach 1- Time complexity - o(n) auxilary space - o(n)

""" def fact(n):
    res = 1
    for i in range(2,n+1):
        res = res * i
    return res

if __name__=='__main__':
    number = 5
    print(fact(number)) """



""" def fact(n):
    if n == 0:
        return 1
    return n* fact(n-1)

if __name__=='__main__':
    number = 5
    print(fact(number)) """

# gcd of two numbers

# time complexity - O(min(a,b)) 

""" def gcd(a,b):
    result = min(a,b)

    while result:
        if a % result == 0 and b%result==0:
            break
        result-=1

    return result

if __name__ == '__main__':
    a = 98
    b=56
    print(f"GCD of {a} and {b} is {gcd(a,b)}") """

# Another approach
# time complexity - O(max(a,b))
# space complexity - O(1)

""" def gcd(a,b):
    while(a!=b):
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

if __name__ == '__main__':
    a = 98
    b = 56
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found') """

# another approach - 

# Recursive function to return gcd of a and b

# time complexity = O(min(a,b))
# space complexity - O(1)


""" def gcd(a, b):
 
    if a == 0:
        return b
    
    if b == 0:
        return a
    
    if a == b:
        return a
    
    if(a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)



if __name__ == '__main__':
    a = 98
    b = 56
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found') """

# Optimised Aprroach - 
# time complexity = O(min(a,b))
# space complexity - O(1)

""" 
def gcd(a, b):
 
    if b == 0:
        return a
    
    if a==0 : 
        return 
    if a==b:
        return a
    
    if (a>b):
        if a%b ==0:
            return b
        return gcd(a-b,b)
    if (b%a==0):
        return a
    return gcd(a,b-a)


if __name__ == '__main__':
    a = 98
    b = 56
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found') """

# Another approach -Time complexity - o(log(min(a,b)))
#Space Complexity - O(log(min(a,b)))

""" def gcd(a,b):

    if b ==0:
        return a
    return gcd(b,a%b)


if __name__ == '__main__':
    a = 98
    b = 56
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found') """



# in built function
# Time Complexity: O(log(min(a,b))
# Auxiliary Space: O(1)

""" import math

if __name__=='__main__':
    a=98
    b=56
    gcd_result= math.gcd(a,b)
    print(f"The gcd of a and b is : {gcd_result}") """

# LCM of two numbers

# Time complexity - O(n), Space Complexity - O(n)
"""  
def lcm(a,b):
    max_num = max(a,b)
    while True:
        if max_num % a ==0 and max_num % b == 0:
            return max_num
        max_num+=1
    
    return max_num   
    
if __name__ == '__main__':
    a = 98
    b = 2
    print(lcm(a,b)) """

# Another approach

# Time complexity - O(log(min(a,b)))
#Space Complexity - O(log(min(a,b)))

""" def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)


def lcm(a,b):
    return (a*b)// gcd(a,b)


if __name__ == '__main__':
    a = 98
    b = 56
    print(lcm(a,b)) """

# Another approach
# Time complexity - O(a*b)
# Space complexity - O(1)

""" def lcm(a,b):
    max_num = max(a,b)
    min_num = min(a,b)
    
    for i in range(max_num,max_num*min_num+1,max_num):
        if i % min_num == 0:
            return i




if __name__ == '__main__':
    a = 98
    b = 56
    print(lcm(a,b)) """

# prime number

# simple approach - O(n) - for checking single element

""" def isPrime(n):
    if n ==1 or n==0:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True

if __name__ == '__main__':
    n = 10
    
    """


# modified approach - O(n) - for checking single element

""" 

def isPrime(n):
   
   if n ==0 or n==1:
      return n
   
   for i in range(2,int(n**1/2)+1):
      if n%i==0:
         return False
    
   return True
 
 
 
N = 100
for i in range(1,N+1):
    if(isPrime(i)):
        print(i,end=" ") """

# modified approach - (Osqrt(n)) - for checking single element

""" def isPrime(n):
    if n ==0 or n==1:
        return False
    i = 2

    while(i*i<=n):
        if n % i ==0:
            return False
        
        i+=1
        
    return True

N = 100
for i in range(1,N+1):
    if(isPrime(i)):
        print(i,end=" ")  """



# modified approach - (Osqrt(n)) - Space Complexity - constant for checking single element
# checking only numbers 6k+-1 as every prime number greater than 3
# can be expressed in the form 6k+-1


""" def isPrime(n):
    if n==0 or n ==1:
        return False
    
    if n==2 or n==3:
        return True
    
    if n%2==0 or n%3==0:
        return False
    
    i = 5
    while(i*i<=n):
        if n%i==0 or n%(i+2) == 0:
            return False
        i+=6
    return True

N = 100
for i in range(1,N+1):
    if(isPrime(i)):
        print(i,end=" ")  """

""" n = 2
if isPrime(n):
    print("true")
else:
    print('false') """

# Prime Fatorisation of a number

""" def isPrime(num):
    if num==1 or num==0:
        return False
    
    elif num==2 or num ==3:
        return True
    
    if num%2==0 or num%3==0:
        return False
    
    i=5

    while(i*i<=num):

        if num%i == 0 or num% (i+2) == 0:
            return False
        i+=6

    return True



def prime_factors(num):

    for i in range(2,num+1):
        if isPrime(i):
            x = i
            while num%x==0:
                print(i)
                x = x*i


num  = int(input("enter a number : "))
prime_factors(num) """


# divisors of a number
# time complexity - o(n) space complexity - O(1)

""" def printDivisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)

num = int(input("Enter a number : "))
printDivisors(num) """

# divisors of a numbers -Approach 2
# time complexity - O(sqrt(n)) space complexity - o(1)
# in this approach order is not maintained


""" def printDivisors(n):
    i=1
    while(i*i<=n):
        if n%i==0:
            print(i)
            if i != n/i:
                print(n//i)
        i+=1
num = int(input("Enter a number : "))
printDivisors(num)

 """

# another approach - theta(sqrt(n))
""" 
def printDivisors(n):
    i=1
    while(i*i< n):
        if n%i==0:
            print(i)
        i+=1

    while(i>=1):
        if n%i==0:
            print(n//i)
        i-=1



num = int(input("Enter a number : "))
printDivisors(num) """

# sieve of eratosthenes

# prime numbers from 1 to n

# time complexity - o n*(sqrt(n))



""" def isPrime(n):
    if n ==1:
        return False
    
    if n==2 or n==3:
        return True
    
    if n%2 ==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        
        i+=6
    return True

def printPrime(num):
    for i in range(2,num+1):
        if isPrime(i):
            print(i,end=' ')
        
if __name__  == '__main__':
    n=14
    printPrime(n)
 """

# prime numbers from 1 to n

# time complexity - o (sqrt(n))

# space complexity - O(n)

""" def sieve(n):
    if n<=1:
        return 
    is_prime = [True]*(n+1)
    i =2
    while i * i <=n:
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j] = False
        i+=1

        for i in range(2,n+1):
            if is_prime[i]:
                print(i,end=' ')

if __name__=='__main__':
    n = 18
    sieve(n)

 """

# prime numbers from 1 to n

# time complexity - o n*(loglog(n))

# space complexity - O(n)

""" 
def sieve(num):

    if num<=1:
        return 
    is_prime = [True]* (num+1)

    i=2
    while i*i<=num:
        if is_prime[i]:
            for j in range(i*i,num+1,i):
                is_prime[j] = False

        i+=1
    for i in range(2,num+1):
        if is_prime[i]:
            print(i,end=' ')


if __name__ == '__main__':
    num=16
    sieve(num) """

# computing power

# naive solution

# time complexity - O(n)
# space complexity - o(1)

""" 
def computing_power(num,power):
    res = 1
    for i in range(1,power+1):
        res = res*num
    return res
        


num = int(input("Enter a number "))
power = int(input("Enter the power "))

print(computing_power(num,power)) """

# optimised solution
# recursive solution - naive
# time complexity - o(n)
# space compexity - 0(n)

""" def computing_power(num,power):
    if power ==0:
        return 1
    
    return computing_power(num,power-1)*num
        


num = int(input("Enter a number "))
power = int(input("Enter the power "))

print(computing_power(num,power)) """

# optimised solution
# recursive solution - optimised

# time complexity - O(log power)
# space complexity - o(log power)


""" def computing_power(num,power):
    if power ==0:
        return 1
    
    if power % 2 == 0:
        return computing_power(num,power//2) * computing_power(num,power//2)
    
    return computing_power(num,power-1)*num
        


num = int(input("Enter a number "))
power = int(input("Enter the power "))

print(computing_power(num,power)) """


# optimised solution
# recursive solution - more optimised

# time complexity - O(log power)
# space complexity - o(log power)

""" 

def computing_power(num,power):
    if power ==0:
        return 1
    
    res = computing_power(num,power//2) 
    
    if power % 2 == 0:
        return res * res
    
    return computing_power(num,power-1)*num
        


num = int(input("Enter a number "))
power = int(input("Enter the power "))

print(computing_power(num,power)) """


# iterative solution of power of a number (Binary Exponentitation)

# time complexity - O(log power)
# space complexity - o(1)

""" def computing_power(num,power):
    res = 1
    while power>0:
        if power %2!=0: # n$1
            res = res*num
        
        num=num*num
        power = power//2 # power>>1

    return res



num = int(input("Enter a number "))
power = int(input("Enter the power "))

print(computing_power(num,power))  """

# number of trailing zeroes

# time complexity - O(log5(num)) 

# space complexity - o(1)

""" def trailing_zeroes(num):
    res = 0
    i = 5
    while(num/i>=1):
        res += num//i
        i = i*5
    return res



num = int(input("Enter a number : "))

print(trailing_zeroes(num))
 """

# digits in factorial
# time complexity - O(num)
# space compexity -  O(log(fact))

""" def factorial(num):
    res = 1
    for i in range(num,1,-1):
        res = res*i
    return res

def digits_in_factorial(num):
    fact = factorial(num)
    n = len(str(factorial(num)))
    count = 0

    while n>0:
        
        fact = fact//10
        count+=1
        n-=1

    return count
        


num = int(input("Enter a number : "))

print(digits_in_factorial(num)) """


# digits in factorial
# time complexity -O(num * log(num))
# space compexity -  O(1)

""" import math

def digits_in_factorial(num):
    if num<0:
        return 0
    
    if num<=1:
        return 1
    
    digits = 0
    
    for i in range(2,num+1):
        digits += math.log10(i)

    return math.floor(digits)+1

    

num = int(input("Enter a number : "))

print(digits_in_factorial(num)) """


# numberwith3divisors

# Time Complexity: O(N*log(log(N)))
# Auxiliary Space: O(N)

""" def numbersWith3Divisors(N):
    prime = [True]* (N+1)
    prime[0] = prime[1] = False
    p=2

    while(p*p<=N):
        if prime[p] == True:
            for i in range(p*2,N+1,p):
                prime[i] = False

        p+=1

    
    i=0
    while(i*i<=N):
        if prime[i]:
            print(i*i,end=' ')
        i+=1



# Driver code
if __name__ == "__main__":
    N = 96
 
    # Function call
    numbersWith3Divisors(N) """

# time complexity -  O(sqrt(N)).

# space complexity - O(1) 

""" def numbersWith3Divisors(N):

    i  = 2
    while(i*i<=N):
        if (isPrime(i)):
            print(i*i,end=" ")
        i+=1

def isPrime(N):
    i = 2
    while i*i <= N:
        if N%i == 0:
            return False
        i+=1

        return True
    
if __name__ == '__main__':
    N = 122
    numbersWith3Divisors(N)
 """


# roots of a quadratic equation

import math 
 
 
# function for finding roots
def equationroots( a, b, c): 
 
    dis = b*b - 4*(a*c)

    sqrt_val = math.sqrt(abs(dis))

    if dis>0:
         print('roots are real and different')
         print((-b+sqrt_val)/(2*a))
         print((-b-sqrt_val)/(2*a))

    elif dis == 0:
         print('real and same roots')
         print(-b/(2*a))

    else:
         print(-b/(2*a),sqrt_val)
         print(-b/(2*a),sqrt_val)

# Driver Program 
a = 1
b = 10
c = -24
 
# If a is 0, then incorrect equation
if a == 0: 
        print("Input correct quadratic equation") 
 
else:
    equationroots(a, b, c)