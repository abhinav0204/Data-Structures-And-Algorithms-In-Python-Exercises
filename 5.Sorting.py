# Sorting in python

### Sort()
## Works only for list
## Sorts in-place

### Sorted()

## Works for any iterable
## Does not modify the passed container. Returns a list of sorted items.

## Both uses tim sort and  both are stable - nlogn time complexity

## List Sort() in python
""" 
l1 = [5,10,15,1]
l1.sort()
print(l1)

l2 = [1,5,3,10]
l2.sort(reverse=True)
print(l2)

l3 = ["gfg","ide","courses"]
l3.sort()
print(l3) """


""" def myFun(s):
    return len(s)

l = ["gfg", "courses", "python"]
l.sort(key=myFun,reverse=True)
print(l) """

# Sorting with user defined objects

""" class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def myFun(p):
    return p.x
    
l = [Point(1,15), Point(10,5), Point(3,8)]
l.sort(key = myFun)

for i in l:
    print(i.x, i.y)
 """

## Sorting user defined objects

""" class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def __lt__(self,other):
    return self.x < other.x
    
l = [Point(1,15), Point(10,5), Point(3,8)]
l.sort()

for i in l:
    print(i.x, i.y) """


## Sorting user defined objects -- more cases
""" 
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __lt__(self,other):
        if self.x == other.x:
            return self.y < other.y
        
        else:
            return self.x < other.x
        
l = [Point(1,15), Point(10,5), Point(1,8)]
l.sort()

for  i in l:
    print(i.x , i.y) """


## Sort() in python
## -- Uses tim sort --  hybrid of merge and insertion sort
## -- Stable
## Works only for lists -- as lists are mutable
## Modifies the sort lists

##  Sorted in python

# Works for any iterable (list, Tuple, Dictionary, Strings, Sets)

# Returns a list with sorted items

# Parameters like reverse and key works same way as sort()

""" l = [10,-15,-2,1]
ls = sorted(l, key = abs , reverse=True)
print(ls) """


# Sorted in python
""" 
t = (10, 12, 5, 1)
print(sorted(t))

s = ["gfg", "courses", "python"]
print(sorted(s))

st = "gfg"
print(sorted(st))

d = {10:"gfg", 15:"ide", 5:"courses"}
print(sorted(d))

l = [(10,15), (1,8), (2,3)]
print(sorted(l, key = lambda x:x[1], reverse=True))
 """

## Stability in Sorting Algorithm

## Stabillity - if two items have same values they should appear in the same order as in the original array
## two elements with same value, order remains the same


## input - [("Anil",50),("Ayan",80),("Piyush",50),("Ramesh",80)]

## Stable sorting algo output - [("Anil",50),("Piyush",50),("Ayan",80),("Ramesh",80)]

## Stablitity - only important for an array of mutiple fields (more than one), not useful for a list of integers

## Example Stable sorting algorithms - Bubble Sort, Insertion Sort, Merge Sort
## Example Unstable sorting algorithms - Selection sort, quick sort, heap sort

""" 
arr = [("Anil",50),("Ayan",80),("Piyush",50),("Ramesh",80)]

print(arr) """

## Bubble Sort

# time complexity - O (n^2)
# space complexity - O (1)

""" 
def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

    return l

l = [20,30,22,66,11,64]
print(bubble_sort(l)) """

## Bubble sort - optimised

""" 
def bubble_sort(l):
    n = len(l)

    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                swapped = True

        if swapped == False:
            return l

    return l

l = [2,1,3,4,5]
print(bubble_sort(l)) """

# Stability - Bubble sort is stable as it does not  swap same elements are don't change the order of same elements

# Applications of Bubble sort

# Does not have any practical implementation - generally taught in academics as first sorting algorithm
#  If you are asked to sort the elements only by swapping then bubble sort can be used and is stable and without using extra space



## Selection Sort

# time complexity - O (n^2)
# space complexity - O (1)

# Does less memory writes compared to other algorithms like quick sort,merge sort, insertion sort
# Cycle sort iss optimal in terms of memory writes

# Basic idea for heapsort is stable

# Not Stable

# In-place

""" 
def selectsort(l):
    n = len(l)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if l[j] < l[min_index]:
                min_index = j

        l[min_index],l[i] = l[i],l[min_index]
         """

## Insertion Sort in Python

## O (n^2) worst case
## In place and stable
## Used in practice for small arrays ( timsort and intrasort)
## O(n) in best case

