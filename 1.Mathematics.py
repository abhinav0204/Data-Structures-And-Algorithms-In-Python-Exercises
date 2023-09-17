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
    turn False
    
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

 ## absolute value of a number
""" 
class Solution:
    def absolute(self,I):
        # code here
        if I < 0 :
            return -1 * I
        return I


#{ 
 # Driver Code Starts.
def main():
    T = int(input()) #Input the number of testcases
    while(T > 0):
        I = int(input()) #input number
        ob=Solution()
        print(ob.absolute(I)) #Call function and print
        T -= 1 #Reduce number of testcases


if __name__ == "__main__":
    main() """

## celsius to fahrenheit program

#{ 
 # Driver Code Starts
#Initial Template for Python 3

""" import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    ##Complete this function
    def cToF(self,C):
        #Your code here
        return (((9/5) * C) +32)
        


#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        C=int(input())
        ob=Solution()
        print(math.floor(ob.cToF(C)))
        T-=1
    
    




if __name__=="__main__":
    main()
 """


 ## number of digits in a factorial

 ## basic approach - O (n) - time and space complexity
""" 
def countDigitsInFactorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i

    count = 0
    while fact > 0:
        count+=1
        fact = fact//10
    
    return count

if __name__ == '__main__':
    num = int(input("Enter a number : "))
    print(countDigitsInFactorial(num))

 """

## logrithmic approach - nlogn - time compelxity
""" 
import math

def findDigits(n):
  
  if n < 0 :
    return 0
  
  if n<=1:
    return 1
  
  digits = 0
  for i in range(2,n+1):
    digits += math.log10(i)

  return math.floor(digits)+1

if __name__ == "__main__":
  n = int(input("Enter a number : "))
  print(findDigits(n)) """


## stirilng's formula -- time complexity - 1 

""" import math

def countDigitsInFactorial(n):

    if n < 0:
        return 0
    
    if n<= 1:
        return 1
    
    digits =  math.floor(0.5 * math.log10(2 * math.pi * n) + n * math.log10(n/math.e)) + 1

    return digits

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(countDigitsInFactorial(n))

 """


## count number of primes

# Prime Generation: O(N log(log N))
# Counting Primes: O(√N)
# Overall Time Complexity: O(N log(log N))
""" 
def numbersWithDivisors(N):

    prime = [True] * (N+1)
    prime[0] = prime[1] = False
    p = 2
    while(p * p <= N):

        if (prime[p] == True):

            for i in range(p*2,N+1,p):
                prime[i] = False

        p+=1

    i = 0
    while(i*i <= N):
        if prime[i]:
            print(i*i,end=' ')
        i+=1

if __name__ == '__main__':
    num = int(input("Enter a number : "))
    numbersWithDivisors(num) """

## count number of primes - optimised

# Prime Generation: O(√N log(log √N)) = O(√N log(log N))
# Counting Primes: O(√N)
# Overall Time Complexity: O(√N log(log N))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

""" 
import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    def exactly3Divisors(self,N):
        # code here
        # Optimized Sieve of Eratosthenes
        def sieve_of_eratosthenes(N):
            is_prime = [True] * (N+1)
            is_prime[0] = is_prime[1] = False
            p = 2
            while (p * p <= N):
                if is_prime[p]:
                    for i in range(p * 2, N+1, p):
                        is_prime[i] = False
                p += 1
            return is_prime

        # Generate a list of primes up to sqrt(N)
        primes = sieve_of_eratosthenes(int(N**0.5))

        # Count primes
        count = sum(primes)

        return count

#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        ob=Solution()
        print(ob.exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
# } Driver Code Ends """


## program to find the roots of a quadratic equation

""" import math

def findRoots(a,b,c):

    if a == 0:        # If a is 0, then equation is not quadratic, but linear
        print("Invalid")
        return -1
    
    
    d = b*b - 4 *a*c
    sqrt_val = math.sqrt(abs(d))

    if d> 0 :
        print(math.floor((-b +sqrt_val)/(2*a)),end=' ')
        print(math.floor((-b - sqrt_val)/(2*a)))


    elif d == 0:
        print(math.floor(-b/(2*a)),end=' ')
        print(math.floor(-b/(2*a)))


    else: 
        print(math.floor((-b+sqrt_val)/(2*a)))
        print(math.floor((-b+sqrt_val)/(2*a)))





if __name__ == '__main__':
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    num3 = int(input("Enter the third number : "))
    findRoots(num1,num2,num3) """




## program to find the roots of a quadratic equation

# sorted order of outputs in ascending order

""" import math
class Solution:
    def quadraticRoots(self, a, b, c):
        if a == 0:        # If a is 0, then equation is not quadratic, but linear
            return ['Imaginary']
    
    
        d = b*b - 4 *a*c
        sqrt_val = math.sqrt(abs(d))

        if d> 0 :
            root1 = math.floor((-b + sqrt_val)/(2*a)) 
            root2 = math.floor((-b - sqrt_val)/(2*a))
            return [max(root1, root2), min(root1, root2)]

        elif d == 0:
            root = math.floor(-b/(2*a))
            return [root , root]


        else: 
            return ['Imaginary']



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a,b,c)
        if len(ans)==1 and ans[0]==-1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()
 """
# } Driver Code Ends


## GP Term 

## naive approach - (a.r^n-1)

import math

def nth_term_of_gp(A,B,N):
    R1 = (B/A)
    return math.floor(A*R1**(N-1))


if __name__ == '__main__':
    A = int(input("Enter the value of a : "))

    B = int(input("Enter the second  term of GP : "))

    N = int(input("Enter the value of N : "))

    print(nth_term_of_gp(A,B,N))

