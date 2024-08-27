# Lists

## left rotate by d places

# direct method

# left rotate by d places

""" l = [10,20,30,40,50]

d = 2

l= l[d:] + l[:d]
print(l) """

# using deque

""" 
from collections import deque
l = [10,20,30,40,60]

d = 2

dq = deque(l)
dq.rotate(-d)
l = list(dq)
print(l) """

# Method 1

# time complexity - O(n*d)

# space complexity - O(1)

""" def leftrotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))

l = [10,20,30,40,50]
d = 3
leftrotate(l,d)
print(l) """


# time complexity - 0(n)
# space complexity - o(1)

""" def reverse(l,b,e):
    while(b<e):
        l[b],l[e] = l[e],l[b]
        b+=1
        e-=1


 """

""" 
def leftrotate(l,d):
    n = len(l)

    # handle d=0 and d more than n

    d = d%n

    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)

l = [10,20,30,40,50]
d = 3
leftrotate(l,d)
print(l) """

# maximum difference of arr[i] -arr[j] such that j>i
# time complexity - O(n^2)



""" import sys

def maxdiff(arr,n):

    res = -sys.maxsize-1

    for i in range(0,n-1):
        for j in range(i+1,n):
            res = max(res,arr[j] - arr[i])

    return res

li = [2,3,10,6,4,8,1]
n = len(li)

print(maxdiff(li,n)) """

# maximum difference 
# time complexity - O(n)

""" import sys


def maxdiff(arr,n):

    res = -sys.maxsize-1
    min_value = sys.maxsize

    for j in range(0,n):
        min_value = min(arr[j],min_value)
        res = max(res,arr[j]- min_value)
        
    return res


arr = [2,3,10,6,4,8,1]
n = len(arr)

print(maxdiff(arr,n)) """

# stock buy and sell - part1

# optimised  solution

# time complexity -- o(n)
# space complexitty - o(1)

def maxprofit(price,n):
    profit = 0
    for i in range(1,n):
        if price[i]> price[i-1]:
            profit= profit + price[i] - price[i-1]

    return profit
price = [1,5,3,8,12]
n = len(price)
print(maxprofit(price,n)) 


# trapping rainwater problem
