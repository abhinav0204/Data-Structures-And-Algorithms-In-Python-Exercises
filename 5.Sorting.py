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
## O(1) auxillary space

## Application

## Used to sort small sized arrays (python timsort switches to insertion sort when sorting small sized  arrays ).


## Insertion Sort in Python

## Time complexity - Best case - Array is  sorted - O(n)
## Time complexity - Best case - Array is reverse sorted - O(n^2)
""" 
def insertionSort(l):
    for i in range(1,len(l)):
        x = l[i]
        j = i-1

        while j >=0 and x<l[j]:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = x
    return l

l = [32,41,73,84,45]
print(insertionSort(l)) 
 """

# Merge Sort Algorithm

# Divide and conquer algorithm 
# Stable aglorithm
# O(n log n) time and O(n) aux space
# well suited for linked lists.Worked in O(1) aux space
# used in external sorting
# In general for arrays, Quicksort outperforms

## naive solution

## does not need the array to be sorted
## time complexity - O(m+n)* log(m+n)
## space complexity - O(m+n)
""" 
def merge(a,b):
    res = a+b
    res.sort()
    return res



a = [10,15,30]
b = [2,20]

print(merge(a,b))

 """

## optimised solution
# array needs to be sorted

## time complexity - O(m+n)
## space complexity - O(m+n)
""" 
def mergeSort(a,b):
    res = []
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i <m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i+=1

        else:
            res.append(b[j])
            j+=1

    while i < m:
        res.append(a[i])
        i+=1

    while j < n:
        res.append(b[j])
        j+=1

    return res

a = [10,15,30]
b = [5,6,6,30,40]

print(mergeSort(a,b))
 """

# Merge Subarrays

# time complexity - O(m+n)
# space compexity - O(m+n)

""" 
a = [10,15, 20, 40, 8, 11, 15]

left = 0
mid = 3
high = 6

# divide into two arrays 
# left - a[low:mid+1]
# right - a[mid+1:high+1]

left = [10, 15, 20, 40]
right = [8, 11, 15]

a = [8, 10, 11, 15, 20, 40, 55]
 """
""" 
def merge(a,low, mid,high):
    left = a[low:mid+1]
    right = a[mid+1 : high+1]

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # equals in left array maintains stability - order is preserved in case of same elements
            a[k] = left[i]
            k+=1
            i+=1
        else:
            a[k] = right[j]
            k+=1
            j+=1
    
    while i < len(left):
        a[k] = left[i]
        k+=1
        i+=1

    while j < len(right):
        a[k] = right[j]
        k+=1
        j+=1

    return a

a = [8, 10, 11, 15, 20, 40, 55]
low = 0
high = len(a)-1
mid = (low+high)//2
print(merge(a, low,mid,high))

 """

# Merge Sort Algorithm

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):

    result = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])

    result.extend(left[j:])

    return result

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
