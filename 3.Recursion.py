# Recursion

""" def fun(n):
    # BASE CASE
    if n <= 0:
        return 
    print("gfg")
    fun(n-1)

fun(3) """

# factorial of a number

""" def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)

print(fact(5)) """

# fibonacci of a number

""" def fibo(n):
    if n==1:
        return 1
    if n==0:
        return 0
    
    return fibo(n-1) + fibo(n-2)

print(fibo(7))

for  i in range(0,7+1):
    print(fibo(i)) """

# implementing tail recusion in python

# recursive method

""" def fun(n):
    if n ==0:
        return 
    print(n)
    fun(n-1)

fun(7) """

# optimised approach - without  (iteration)

""" def fun(n):
    while n!=0:
        print(n)
        n=n-1

fun(7) """

# problem 1
""" def fun(n):
    if n == 0 :
        return 
    print(n)
    fun(n-1)
    print(n)

fun(3) """

# problem 2

""" def fun2(n):
    if n==0:
        return
    fun2(n-1)
    print(n)
    fun2(n-1)

fun2(3) """

# problem 3 -- logarithmic floor value of number

""" def fun(n):
    if n <=1:
        return 0
    else:
        1 + fun(n//2)

print(fun(16))
 """
# problem 4 -- logarithmic floor value of number

""" def fun(n):
    if n<=1:
        return 0
    else:
        return 1+ fun(n//2)
    
print(fun(5)) """

# problem 5 -- convert number to binary bits

""" def fun(n):
    if n == 0:
        return 
    fun(n//2)
    print(n%2)

fun(13) """

# print 1 to n function
# first print and recursion call - 1 to N
## first print and recursion call - N to 1

""" def print1toN(N):
    if N==0:
        return
    print1toN(N-1)
    print(N)


print1toN(3) """


# print n to 1 using recusion

""" def print1toN(n):
    if n==0:
        return
    print(n)
    print1toN(n-1)


n = 3
print1toN(n) """

# Sum of digits using recursion
""" 
def dsum(n):
    if n<10:
        return n
    return dsum(n//10) + n%10

print(dsum(253)) """

# palindrome check using recursion
# time complexity - O(n)
# space complexity - o(n)
""" 
def isPalindrome(str,start,end):
    if start >= end:
        return True
    
    return str[start] == str[end] and isPalindrome(str,start+1,end-1)

str = "abcba"
n = len(str)

print(isPalindrome(str,0,n-1)) """

# fibonacci  using recursion

def fibo(n):
    arr = [0]*(n)
    arr[0] = 0
    arr[1]= 1
    
    for i in range(2,n):
        arr[i] = arr[i-1] + arr[i-2]

    return arr





print(fibo(8))