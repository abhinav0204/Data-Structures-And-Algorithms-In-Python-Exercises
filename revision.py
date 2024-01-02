# sum of n natural number O(1)

""" def natural_number(n):
    return n*(n+1)/2


n = int(input("Enter a number : "))

print(natural_number(n)) """


# sum of n natural number O(n)

""" def natural_number(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total


n = int(input("Enter a number : "))

print(natural_number(n))
 """

# sum of n natural number O(n^2)

def natural_number(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum=sum+1

    return sum

n = int(input("Enter a number : "))

print(natural_number(n))