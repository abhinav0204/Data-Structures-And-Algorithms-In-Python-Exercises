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


