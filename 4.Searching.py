# binary search in python
# time complexity - O(log n)
# space complexity - O (1)

""" def bSearch(l,x):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2

        if l[mid] == x:
            return mid
        
        elif l[mid] < x:
            low = mid+1

        else:
            high = mid-1

    return -1


l = [20,30,40,60,80]
x = 60
print(bSearch(l,x)) """


# Recursive binary search in python
# time complexity - O(log n)
# space complexity - O (log n)
""" 
def bsearch(l,x,low,high):
    if low > high:
        return -1
    
    mid = low + ((high-low)//2)

    if l[mid] == x:
        return mid
    
    elif l[mid] > x:
        return bsearch(l,x,low,mid-1)
    
    else:
        return bsearch(l,x,mid+1,high)
    

l = [10,20,30,40,50]
x = 40
print(bsearch(l,x,0,len(l)-1)) """

## Index of first occurence of the array

# naive approach - single traversal
# time complexity - O(n)
# space complexity - O(1)

""" def firstOccurence(arr,n,x):
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1


l = [10,20,20,20,20,20,30,40,40,50,50]
x = 4
n = len(l)
print(firstOccurence(l,n,x))

 """
## Index of first occurence of the array

# binary search - recursive approach
# time complexity - O(logn)
# space complexity - O(logn)
""" 
def firstOccurence(arr,low,high,x):
    if low > high:
        return -1
    
    mid = (low+high)//2

    if x>arr[mid]:
        return firstOccurence(arr,mid+1,high,x)
    
    elif x<arr[mid]:
        return firstOccurence(arr,low,mid-1,x)

    else:
        if mid == 0 or arr[mid-1] != arr[mid]:
            return mid

        else:
            return firstOccurence(arr,low,mid-1,x)    


l = [10,20,20,20,20,20,30,40,40,50,50]
x = 40
n = len(l)-1
print(firstOccurence(l,0,n,x))
 """
## Index of first occurence of the array

# binary search - recursive approach
# time complexity - O(logn)
# space complexity - O(1)

""" 
def firstOccurence(arr,low,high,x):
    low = 0
    high = n-1
    
    while(low <= high):
        mid = (low+high)//2

        if arr[mid] < x:
            low = mid+1

        elif arr[mid] > x:
            high = mid-1
        
        else:
            if mid == 0 or arr[mid] != arr[mid-1]:
                return mid
            else:
                high = mid-1
    return -1



l = [10,20,20,20,20,20,30,40,40,50,50]
x = 40
n = len(l)-1
print(firstOccurence(l,0,n,x))
 """
## Index of last occurence

# naive approach - single traversal
# time complexity - O(n)
# space complexity - O(1)
""" 
def lastOccurence(l,x):
    for i in reversed(range(len(l))):
        if l[i] == x:
            return i
        
    return -1



l = [10,20,20,20,20,20,30,40,40,50,50]
x = 40
print(lastOccurence(l,x)) """


## Index of last occurence

# alternative approach -recursive bianry search
# time complexity - O(log n)
# space complexity - O(log n)
 
""" 
def lastOccurence(l,low,high,x):

    if low > high:
        return -1
    
    mid = (low+high)//2
    
    if l[mid] < x:
        return lastOccurence(l,mid+1,high,x)
    elif l[mid] > x:
        return lastOccurence(l,low,mid-1,x)
    
    else:
        if mid == len(l)-1 or l[mid] != l[mid+1]:
            return mid
        
        else:
            return lastOccurence(l,mid+1,high,x)





l = [10,20,20,20,20,20,30,40,40,50,50]
x = 10
n = len(l)-1
print(lastOccurence(l,0,n,x)) """


## Index of last occurence

# alternative approach -iterative bianry search
# time complexity - O(log n)
# space complexity - O(1)

""" 
def lastOccurence(l,low,high,x):
    
    while(low <=high):
        mid = (high+low)//2
        
        if l[mid] < x:
            low = mid+1

        elif l[mid] > x:
            high = mid -1

        else:
            if mid == len(l)-1 or l[mid] != l[mid+1]:
                return mid
            else:
                low = mid+1

    return -1
            

l = [10,20,20,20,20,20,30,40,40,50,50]
x = 40
n = len(l)-1
print(lastOccurence(l,0,n,x)) """

# Count occurences in a sorted array
# naive approach - single traversal
# time complexity - O(n)
# space complexity - O(1)

""" def count_occurences(arr,x):
    count = 0
    for ele in arr:
        if ele == x:
            count+=1

    return count


array = [10, 20, 20, 20, 30, 30, 40, 50, 50, 50]
value_to_count = 20
occurences = count_occurences(array,value_to_count)
print(occurences) """

# Count occurences in a sorted array
# optmised approach - binary search
# time complexity -  O(log n) (two binary searches)
# space complexity - O(1)

""" 
def first_occurences(arr,x):
    low = 0
    high = len(arr)-1

    while(low < high):
        mid = (low+high)//2

        if arr[mid] < x:
            low = mid+1
        
        elif arr[mid] > x:
            high = mid-1

        else:
            if arr[mid] == 0 or arr[mid] != arr[mid-1]:
                return mid
            else:
                high = mid-1
    return -1

def last_occurences(arr,x):
    low = 0
    high = len(arr)-1

    while(low <= high):
        mid = (low + high)//2

        if arr[mid] < x:
            low = mid+1

        elif arr[mid] > x:
            high = mid-1
        
        else:
            if mid == len(arr)-1 or arr[mid] != arr[mid+1]:
                return mid
            
            else:
                low = mid+1

    return -1


def count_occurences(arr,x):
    first_occurence = first_occurences(arr,x)

    if first_occurence == -1:
        return 0
    
    else:
        last_occurence = last_occurences(arr,x)
        return last_occurence  - first_occurence +1

array = [10, 20, 20, 20, 30, 30, 40, 50, 50, 50]
value_to_count = 20
n = len(array)
occurences = count_occurences(array,value_to_count)
print(occurences) """


# Count 1's  in a sorted binary list

# naive approach -  single traversal
# time complexity -  O( n)
# space complexity - O(1)
""" 
def count_occurences(array):

    count=0
    for i in reversed(range(len(array))):
        if array[i]!=0:
            count+=1
            


    return count

array = [0, 0, 0, 1, 1, 1, 1, 1]

print(count_occurences(array))
 """

# Count 1's  in a sorted binary list

# optiimised approach -  binary search
# time complexity -  O(log n)
# space complexity - O(1)

""" 
def firstOccurence(arr,x):
    low = 0
    high = len(arr)-1

    while(low < high):

        mid = (low+high)//2

        if arr[mid] < x:
            low = mid+1

        elif arr[mid] > x:
            high = mid-1

        else:
            if arr[mid] == 0 or arr[mid] != arr[mid-1]:
                return mid
            else:
                 high = mid-1

    return -1

def countOccurences(arr,x):
    if firstOccurence(arr,x) == -1:
        return 0
    
    else:
        return len(arr) - firstOccurence(arr,x)

arr = [0,0,0,1,1,1,1]
x = 1

print(countOccurences(arr,x))
 """

## Square Root
# naive approach - single traversal
# time complexity - O(n)
# space complexity - O(1)

""" def square_root(n):
    i = 1
    while i * i <= n:
        i+=1
    
    return i-1

print(square_root(25)) """


# optimised - single traversal
# time complexity - O(log n)
# space complexity - O(1)

""" 
def sqrt_binary_seach(x):
    if x< 0:
        return 0
    
    if x == 1:
        return 1
    
    low,high = 0,x

    ans = -1
    while low <= high:
        mid = (low+high)//2
        mid_squared = mid*mid

        if mid_squared == x:
            return mid
        
        elif mid_squared < x:
            low = mid + 1

        else:
            high = mid - 1
            ans = mid-1

    return ans

print(sqrt_binary_seach(26))
 """


