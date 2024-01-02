# list
""" 
l = [10,20,30,40,50]
print(l)
print(l[3])
print(l[-1])
print(l[-2])

# list functions
l.append(30)
print(l)

l.insert(1,15)
print(l)

print(15 in l)

print(l.count(30))

print(l.index(30))

print(l.index(30,4,7)) """


""" 
l = [10,20,30,40,50,60,70,80]

l.remove(20)
print(l)

print(l.pop(1))
print(l)

print(l.pop(2))
print(l)

del l[1]
print(l)

del l[0:2]
print(l)

 """

""" l = [10,40,20,50]

print(max(l))

print(min(l))

print(sum(l))

l.reverse()

print(l)

l.sort()

print(l)

l = ["efg","abc","gfg","def"]

print(max(l))

print(min(l))

l.reverse()
print(l)

l.sort()
print(l) """

# Average or mean of the list

list = [10,20,30,40]

# 1st approach
""" def avg_of_list(list):
    total=0
    for i in list:
        total+=i
    return total/len(list)

print(avg_of_list(list)) """

# 2nd approach

""" def avg_of_list(list):
    return sum(list)/len(list)

print(avg_of_list(list))  """


#3rd approach
""" def avg_of_list(lst):
    total = sum([i for i in lst])
    return total/len(lst)

print(avg_of_list(list))  """


#1st approach

""" ex_list = [10,41,30,15,80]

def even_odd(ex_list):
    even_list = []
    odd_list = []
    for i in range(len(ex_list)):
        if ex_list[i]%2==0:
            even_list.append(ex_list[i])
        else:
            odd_list.append(ex_list[i])

    return even_list,odd_list

print(even_odd(ex_list)) """

#2nd approach


""" ex_list = [10,41,30,15,80]

def even_odd(ex_list):
    even_list =[]
    odd_list =[]
    for i in ex_list:
        if i %2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return [even_list,odd_list]

print(even_odd(ex_list)) """

#3rd approach

""" ex_list = [10,41,30,15,80]

even_list = [i for i in ex_list if i%2 ==0 ]
odd_list = [i for i in ex_list if i%2!=0]
# even_odd = [[even_list.append(i)] if i%2 == 0 else [odd_list.append(i)] for i in  ex_list ]
print([even_list ,odd_list]) """

#4rth approach

""" ex_list = [10,41,30,15,80]

even_list = []
odd_list = []
even_odd = [[even_list.append(i)] if i%2 == 0 else [odd_list.append(i)] for i in  ex_list ]
print([even_list ,odd_list]) """

# Get smaller elements
""" 
def smaller_element(ex_list,key):
    output_list=[]
    for i in range(len(ex_list)):
        if ex_list[i] < key and ex_list[i] not in output_list:
            output_list.append(ex_list[i])
    return output_list

ex_list = [8,100,20,40,3,7] 
key = 10

print(smaller_element(ex_list,key))

ex_list1 = [100,20,40,60,80,20]
key1 = 60
print(smaller_element(ex_list1,key1)) """


# Slicing (List,Tuple and String)
""" 
l = [10,20,30,40,50]

print(l[0:5:2])

print(l[:4])

print(l[2:])

print(l[4:1:-1])

print(l[-1:-6:-1])

print(l[::-1])

 """


""" l1 = [10,20,30]
l2 = l1[:] # in case of list you always get a different list as output


t1 = (10,20,30)
t2 = t1[:]

s1 ="geeks"
s2 = s1[:]

print(l1 is l2) # both the lists are different
print(t1 is t2) # both the  tuples and strings are same
print(s1 is s2) """

# List Comprehension in Python

""" l1 = [x for x in range(11) if x%2==0]
print(l1)

l2 = [x for x in range(11) if x%2!=0]
print(l2) """


""" 
ex_list = [10,41,30,15,80]

even_list = []
odd_list = []
even_odd = [[even_list.append(i)] if i%2 == 0 else [odd_list.append(i)] for i in  ex_list ]
print([even_list ,odd_list]) 

 """

""" 
ex_list = [8,100,20,40,3,7] 
key = 10

smaller_element = [ex_list[i] for i in range(len(ex_list)) if ex_list[i] <key ]

print(smaller_element)


 """


""" 
s ="geeksforgeeks"

l1 = [x for x in s if x in "aeiou"]

print(l1)

l2 = ["geeks",'ide','courses','gfg']

l3 = [x for x in l2 if x.startswith('g')]

print(l3)

l4 = [x*2 for x in range(6)]
print(l4)

l1 = ["geeks","for","geeks","gfg","ide"]

l2 = [x.upper() for x in l1 if x.startswith("g")]

print(l2)
 """

#set comprehension
""" 
l=[10,20,3,4,10,20,7,3]

s1 ={x for x in l if x%2==0}
s2 = {x for x in l if x%2!=0}
print(s1)
print(s2)

# dictinary comprehension

l1 = [1,3,4,2,5]
d1 = {x:x**3 for x in l1}

print(d1)

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)

l2 = [101,102,103]
l3 = ["gfg","ide","courses"]
d3 = {l2[i]:l3[i] for i in range(len(l3))}
print(d3) 


l2 = [101,102,103]
l3 = ["gfg","ide","courses"]
d3 = dict(zip(l2,l3))
print(d3)


# inverted dictionary

d1 = {101:'gfg',103:'practice',102:'ide'}

d2 = {v:k for (k,v) in d1.items()}

print(d2)

"""
# largest element in the list

""" def largest(l):
    return max(l)

l = [10,5,20,9]
print(largest(l)) """


""" def largest2(l):
    for x in l:
        for y in l:
            if y>x:
                break
        else:
            return x
        
    return None



l = [10,5,20,9]
print(largest2(l)) """

""" 

def largest(l):
    max_val = -2147483648
    for i in l:
        max_val = max(max_val,i)
    return max_val


l = [10,5,20,9]
print(largest(l)) """


""" def largest(l):
    if not l:
        return None
    
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i] > res:
                res = l[i]

        return res




l = [10,5,20,9]
print(largest(l)) """

# Second largest element in a list

# Naive approach - O(n)

def getMax(l):
    res = l[0]
    for i in range(1,len(l)):
        res = max(res,l[i])
    return res


def second_largest(ex_list):

    if len(ex_list) <=1:
        return 'Invalid input' 
    
    largest = getMax(ex_list)
    second_largest = None

    for i in ex_list:
        if i != largest:
            if second_largest == None:
                second_largest = i

            else:
                second_largest = max(i,second_largest)

    return second_largest

ex_list = [5,20,12,10,20,10,12]
print(second_largest(ex_list))


# first approach - O (nlogn)
""" 
def second_largest(ex_list):
    ex_list.sort(reverse=True)

    for i in range(1,len(ex_list)):
        if (ex_list[i] != ex_list[0]):
            return f'The second largest element is {ex_list[i]}'
        else:
            return 'There is no largest element in the list !'

# second largest - 

ex_list = [10,5,8,20]
print(second_largest(ex_list))

 """

# second approach - O (n)

""" def second_largest(l):

    if len(l)<2:
        return "Invalid input"
    
    largest = second_largest = -2454635434

    for i in range(0,len(l)):
        largest = max(largest,l[i])


    for i in range(0,len(l)):
        if l[i] != largest:
            second_largest = max(second_largest,l[i])

    
    if second_largest == -2454635434:
        return "There is no second largest element"

    else:
        return f'The second largest element is {second_largest}'
    

ex_list = [10,5,8,20]
print(second_largest(ex_list)) """

# third approach - O(n)
""" 
def second_largest(l):
    if len(l) < 2:
        return 'Invalid input'
    
    largest = second_largest = -2454635434

    for i in range(len(l)):
        if l[i] > largest:
            second_largest = largest
            largest = l[i]

        if l[i] != largest and l[i] > second_largest:
            second_largest = l[i]
    
    if second_largest == -2454635434:
        return "There is no largest second element"
    
    else:
        return f'The second largest element in the list is {second_largest}'

l = [10,10,10]
print(second_largest(l))
 """

# check if the list is sorted or not

# approach 1 - O(n)

""" def isSorted(l):
    i=1
    while(i < len(l)):
        if l[i] < l[i-1]:
            return False
        i+=1
    return True
    

l = [10,20,30,35,40]
if isSorted(l):
    print("Yes")
else:
    print("No")

 """

# Approach 2- n log n


""" def isSorted(l):
    if l == sorted(l):
        return True
    else:
        return False


l = [10,20,30,15,40]
if isSorted(l):
    print("Yes")
else:
    print("No")
 """


# Approach 3- O(n)

""" 
def isSorted(l):
    return all(l[i] >= l[i-1] for i in range(1,len(l)))



l = [10,20,30,15,40]
if isSorted(l):
    print("Yes")
else:
    print("No") """


# reverse a list
""" 
l = [10,20,30]
l.reverse()
print(l)

l = [10,20,30]
new_l = l[::-1]
print(new_l)



l = [10,20,30]
new_l = list(reversed(l))
print(new_l)
 """

# manual way - reversing a list

""" def reverse_list(l):
    start = 0
    end = len(l)-1

    while(start < end):
        temp  = l[start]
        l[start] = l[end]
        l[end] = temp
        start+=1
        end-=1
    return l

l=[1,2,3,4,5,6,7]
print(reverse_list(l)) """



""" 
def reverse_list(l):
    start = 0
    end = len(l)-1

    while(start < end):
        l[start],l[end]= l[end],l[start]
        start+=1
        end-=1

    return l

l=[1,2,3,4,5,6,7]
print(reverse_list(l))  """


# remove duplicates from sorted array - Important

def remove_duplicates(arr,n):
    temp = [0] * n
    temp[0] = arr[0]
    res = 1
    for i in range(1,n):
        if temp[res-1]!=arr[i]:
            temp[res]= arr[i]
            res+=1
    for i in range(0,res):
        arr[i] = temp[i]
    return res

arr = [10,20,20,30,30,30,30]
n = len(arr)
print(remove_duplicates(arr,n))
