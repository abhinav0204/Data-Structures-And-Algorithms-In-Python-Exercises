# strings - sequence of characters
# character A to Z - 65 to 90
# character a to z - 97 to 122

# ord - char to asii value

""" print(ord("a"))

print(ord("A"))
 """
# char - ascii value to character

""" print(chr(97))

print(chr(65)) """

""" 
s = "geek"

print(s)

print(s[-1])

print(s[-2])

print(s[1]) """


# strings are immutable

""" s = 'geek'
s[0] = 'e'
print(s) """


"""
s = ''' Hi, "Abhinav",
    This is python Course
    How you are enjoying it. '''

print(s)

"""
""" 
s = 'Welcome to Geek\'s Course'

print(s)

s = "Hi , \n Welcome to the course"
print(s) """


# Escape sequence and raw strings
""" 
s1 = "A simple \ example"

print(s1)

s2 = "Backslash at the end \\"

print(s2)

s3 = "\\n"

print(s3)

s4 = "\\t"

print(s4) """


# raw strings in python
""" 
s1 = "D:\coding\geeks for geeks python\\7.strings.py"

print(s1)

s1 = r"D:\coding\geeks for geeks python\\7.strings.py"
print(s1) """


# formatted strings in python

# using % 

""" name  = "Abhinav"
course = "Python course"

s = "Welcome %s to the %s"%(name,course)
print(s)
 """
# using format string
""" 
name = "abhinav"
course = "Python course"

s = "Welcome {0} to the {1} using formatted string".format(name,course)

print(s) """

# using f-string -- from python 3.6

""" name = "abhinav"
course = "Python course"

s = f" Welcome {name} to the {course} using f-string" """


""" a = 10
b = 20

print(f"Sum of {a} and {b} is {a+b}")

print(f"Product of a and b is {a*b}") """


""" s1 = "ABC"
s2 = "abc"

print(f"lower case of {s1} is {s1.lower()}")

print(f"Upper case of {s2} is {s2.upper()}") """

# string comparison in python
""" 
s1 = "geeksforgeeks"

s2 = "ide"

print(s1 < s2)

print(s1 > s2)

print(s1 == s2) """


#  string operations in python

""" s1 = "geeksforgeeks"
s2 = "geeks"
print(s2 in s1)
print(s2 not in s1)

s3 = s1 + s2

s4 = "welcome to " + s1 + s2

print(s3)

print(s4)
 """

""" s1 = "geeksforgeeks"
s2 = "geeks"

print(s1.index(s2))

print(s1.rindex(s2))  # next index of s2 in s1 

print(s1.index(s2,0,13))  # start and end index+1 """


# string operations 2

""" s1 = 'geeks'


print(len(s1))

print(s1.upper())

print(s1.lower())

print(s1.islower())

print(s1.isupper()) """

""" 
s = "GeeksforGeeks Python Course"

print(s.startswith("Geeks"))

print(s.endswith("Course"))

print(s.startswith("Geeks",1)) # start index

print(s.startswith("Geeks",8,len(s))) # start and end_index+1 """


# split -- split string into list

""" s1 = "GeeksforGeeks Python Course"

print(s1.split())

s2 = "geeks, for, geeks"

print(s2.split(","))
 """
# join - join list to string
""" 
l = ["geeksforgeeks", "python", "lower"]

print(" ".join(l))

print(",".join(l))

print("@".join(l)) """

# strip,lstrip,rstrip

""" 

s = "---geeksforgeeks----"

print(s.strip("-"))

print(s.lstrip("-"))

print(s.rstrip("-")) """


"""

s1 = "geeksforgeeks"

s2 = "geeks"
 
print(s1.find(s2))

print(s1.find("gfg"))

n = len(s2)

print(s1.find(s1,1,n)) # start and end_index+1 """


# reverse a string in python

""" s = input("Enter a string : ")

rev = ""

for i in s:
    rev  = i+rev
print(rev) """

""" s = input("Enter a string : ")
print(s[::-1]) """

# check for rotation
""" 
def arrrotation(s1,s2):
    if len(s1) != len(s2):
        return False
    
    temp = s1 + s1
    return temp.find(s2)!=-1

s1 = "ABCD"
s2 = "CDAB"


S3 = "ABAAA"
S4 = "BAAAA"
print(arrrotation(s1,s2))

print(arrrotation(S3,S4)) """

""" 
def is_pali(s):

    low = 0
    high = len(s)-1

    while low < high:
        if s[low] != s[high]:
            print("No")
            break
        
        low+=1
        high-=1
    else:
        print("Yes")


     
s = input("Enter a string :  ")
is_pali(s)
 """


""" 
def is_pali(s):
    return s == s[::-1]


print(is_pali("madam"))
print(is_pali("abhinav")) """


# total number of subsequence in a string - 2^n
# subsequence - don't need to continuous but in same order
# substring - needs to be in same order

""" 
def inSubseq(s1,s2):
    i=j=0

    while(i<len(s1) and j < len(s2)):
        if s1[i] == s2[j]:
            j+=1
        i+=1

    if j == len(s2):
        return True
    else:
        return False
    

print(inSubseq('ABCDEF','ADE')) """

""" def inSubseq(s1,s2,m,n):
    if n == 0:
        return True
    # if string 2 is fully traversed or empty string
    
    if m == 0:
        return False
    
    if s1[m-1] == s2[n-1]:
        return inSubseq(s1,s2,m-1,n-1)

    else:
        return inSubseq(s1,s2,m-1,n)
    

print(inSubseq('ABC','AC',3,2)) """

# check for anagram

# anagram -- every word in string 1 also present in string2
# number of characters should be same in both the strings
# example - s1 - listen , s2 - silent

# naive solution - nlogn

""" 
def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2


print(is_anagram('listen','silent')) """

""" 
def isanagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    count =[0]*256

    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1

    for i in count:
        if i != 0:
            return False
        
    return True


print(isanagram("abcd","bacd")) """


""" 
test_str = "GeeksforGeeks"

all_freq = {}

for i in test_str:
    all_freq[i] = all_freq.get(i,0)+1
    
print(all_freq) """

"""   
s1 = "dab"
s2 = "bad"

char_list1 = list(s1)
char_list2 = list(s2)

char_count = {}

for char in char_list1:
    if char not in char_count:
        char_count[char]=0
    
    char_count[char]+=1

for char in char_list2:
    if char not in char_count.keys():
        print("The strings are not anagrams")
        break
    else:
        char_count[char]-=1

else:
    for count in char_count.values():
        if count != 0:
            print("The strings are not anagram")
            break
    else:
        print("the strings are anagram") """

# leftmost repeating characters

# naive approach - O(n^2)
""" 
def leftmost_repeating_char(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return i
            
    return -1

print(leftmost_repeating_char('cabbbad')) """


# efficient approach

# time complexity - o(n)
# space complexity - O(1)

""" def left_most_character(s):
    count = [0] * 256

    for i in range(len(s)):
        count[ord(s[i])]+=1



    for i in range(len(s)):
        if count[ord(s[i])]>1:
          
            return i
        
    


print(left_most_character('abcdb'))

 """

# time complexity - O(n) space complexity - O(1)
""" 
import sys

CHAR = 256

def  leftmost_occurence(str):
    fIndex = [-1] * CHAR
    res = sys.maxsize

    for i in range(len(str)):
        if(fIndex[ord(str[i])]==-1):
            fIndex[ord(str[i])]= i
        
        else:
            res = min(res,fIndex[ord(str[i])])

    if res == sys.maxsize:
        return -1
    else:
        return res
    
print(leftmost_occurence('abccabd')) """


# time complexity - O(n) space complexity - O(1) (less comparisons)


""" 
CHAR = 256

def leftmost_character(str):
    visited = [False] * CHAR
    res = -1

    for i in range(len(str)-1,-1,-1):
        if visited[ord(str[i])] == True:
            res = i
        else:
            visited[ord(str[i])]= True
    return res

print(leftmost_character('abcbcd'))
         """

# left most non repeating character
""" 
def left_most_non_repeating(str):
    
    for i in range(len(str)):
        flag = False
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                flag = True
                break
        if flag == False:
            return i
        
    return -1

print(left_most_non_repeating('geeksforgeeks'))


 """

# leftmost non repeating character

# time complexity - O(n)

# space complexity - O(char)


""" 
CHAR = 256

def nonRepeating(string):
    count = [0] * CHAR
    for i in range(len(string)):
        count[ord(string[i])]+=1

    for i in range(len(string)):
        if count[ord(string[i])]==1:
            return i

    return -1

print(nonRepeating('abbacd'))

 """


# time complexity - O(n + char)

# space compexity - o(char)
""" 
import sys

CHAR = 256
import sys

def print_repeating_characters(string):
    fi = [-1] * CHAR
    for i in range(len(string)):
        if fi[ord(string[i])] ==-1:
            fi[ord(string[i])] = i
        else:
            fi[ord(string[i])] = -2

    res = sys.maxsize

    for i in range(len(fi)):
        print(fi[i])
        if fi[i] >= 0:
            res = min(res,fi[i])
    
    if res == sys.maxsize:
        return -1
    return res

print(print_repeating_characters('abbcbda')) """

#  reverse words in a string
""" 
def reverse_words_in_string(s):
    words = s.split(' ')
    reverse_word  = words[::-1]
    return ' '.join(reverse_word)

print(reverse_words_in_string('welcome to abhinav pc'))
 """

# time complexity - o(n)
# space complexity - o(n)
""" 
def reverse_words_in_string(s):
    words = s.split(' ')
    reverse_word  = words[::-1]
    return ' '.join(reverse_word)

print(reverse_words_in_string('welcome to abhinav pc')) """


# time complexity - O(n)
# space complexity - o(n)
""" 
def reverse(s,b,e):
    while(b<e):
        s[b],s[e] = s[e],s[b]
        b+=1
        e-=1


def reverse(s, b, e):
    while b < e:
        s[b], s[e] = s[e], s[b]
        b += 1
        e -= 1

def reverseWords(s):
    # Convert string to a list of characters to make it mutable
    s_list = list(s)
    n = len(s_list)
    b = 0
    for e in range(n):
        if s_list[e] == ' ':
            reverse(s_list, b, e-1)
            b = e + 1
    reverse(s_list, b, n-1)  # reverse the last word
    reverse(s_list, 0, n-1)  # reverse the entire list to get words in correct order

    # Convert the list of characters back to a string
    return ''.join(s_list)

s = "Welcome to dsa"
print(reverseWords(s)) """


