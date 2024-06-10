# problems with array

# either size is fixed and pre allocated (in both fidxed and variable size array),
# or the worst case insertion at the end is O(n)

#insertion at the middle is costly (or beggining is costly)

# deletion from the middle element (or beginning) is costly

# selection from the middle element (on beginning) is costly

# implementation of data structures like queues and deque is complex with arrays

# head and reference - reference of last node is none

# drop contiguos memory requrirement so that insert and delete happen faster

# linked list advantage -

# ease of insertion and deletion

# disadvantage - no random access, not cache friendly

""" 
class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


    def printList(self):
        current = self
        while current:
            print(current.key , end="-->" if current.next else "")
            current = current.next
 """

""" temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next = temp2

temp2.next = temp3
 """

# alternative appraoch
""" 
head = Node(10)

head.next = Node(20)

head.next.next = Node(30)

head.printList() """

""" class Node:
    def __init__(self,k):
        self.key = k
        self.next  = None

    def printList(self):
        current = self
        while(current):
            print(current.key,end='-->'if current.next else '')
            current = current.next

 """


""" temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next = temp2

temp2.next = temp3 """

# Another approach

""" head =  Node(10)

head.next = Node(20)

head.next.next = Node(30)

head.printList() """

# applications of linked list

# 1) worst case insertion at the end and begin are o(1)

# 2) worst case deletion from the begnning is o(1)

# 3) insertions and deletions in the middle are o(1) if we
# have the reference to the previous node

# 4) round robin implementation - circular linked list

# 5) merging two sorted linked list is faster than arrays

# 6) implementation of simple memory manager where we need to link free blocks

#7 easier implementation of queue and deque data structures

# traversing the linked list

# time compexlity - o(n) for n nodes
# aux space complexity - o(1)
""" 
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

    def printList(head):
        curr = head
        while curr != None:
            print(curr.key,end=' ')
            curr= curr.next

head = Node(10)
head.next = Node(20)
head.next.next  = Node(15)
head.next.next.next = Node(30)

Node.printList(head) """

""" 
class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

    def search(head,x):
        pos=1
        curr = head
        while curr != None:
            if curr.key == x:
                return pos
            pos +=1
            curr = curr.next

        return -1


head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(30)
postion = Node.search(head,50)
print(postion) """


# Insert at end of linked list
# TIME COMPLEXITY - O(N)
# SPACEE COMPLEXITY - O(1)
""" class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

    def insertBegin(head,key):
        temp =Node(key)
        temp.next = head
        return temp
    
    def printList(head):
        curr = head
        while curr is not None:
            print(curr.key,end="-->"if curr.next else '')
            curr = curr.next
    

head = None
head = Node.insertBegin(head,10)
head = Node.insertBegin(head,20)
head = Node.insertBegin(head,30)

Node.printList(head)
 """


# insert at end

# time compexity - O(n)
# space comlexity -O(1)
""" 
class Node:

    def __init__(self,key):
        self.key = key
        self.next = None

    def insertAtEnd(head,key):
        if head == None:
            return Node(key)
        
        curr = head
        while curr.next != None:
            curr = curr.next
        
        curr.next = Node(key)
        return head
    
    def printList(head):
        curr = head
        while curr is not None:
            print(curr.key,end="-->"if curr.next else '')
            curr = curr.next

head = None
head = Node.insertAtEnd(head,10)
head = Node.insertAtEnd(head,20)
head = Node.insertAtEnd(head,30)
Node.printList(head)
 """

# insert at given position

# time compexity - O(min(position,n))
# space comlexity -O(1)

""" class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

    def insertPos(head,data,pos):
        temp = Node(data)
        if pos == 1:
            temp.next = head
            return temp
        
        curr = head

        for i in range(pos-2):
            curr = curr.next
            if curr == None:
                return head
            
        temp.next = curr.next
        curr.next = temp
        return head
    
    def printList(head):
        curr = head
        while curr is not None:
            print(curr.key,end="-->"if curr.next else "")
            curr = curr.next


head = Node(10)

head.next = Node(20)

head.next.next = Node(30)

head.next.next.next = Node(40)

head.next.next.next.next = Node(50)

Node.insertPos(head,45,4)
Node.printList(head)
 """

# delete first node in linked list
# time complexity - O(1)
# space complexity - O(1)
""" 
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

    def delFirst(head):
        if head == None:
            return None
        else:
            return head.next
        

    def printList(head):
        curr = head
        while curr is not None:
            print(curr.key,"-->"if curr.next else "")
            curr = curr.next


head = Node(10)
head = Node.delFirst(head)
# head.next = Node(20)
# head.next = Node(30)

Node.printList(head)
 """

# delete last node

# time complexity - o(n)
# space complexity - o(1)
""" 
class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

    def deleteLastNode(head):
        if head == None:
            return None
        
        if head.next == None:
            return None
        

        # finding second last node
        curr = head
        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        return head
    
    def printList(head):
        curr = head
        while curr is not None:
            print(curr.key,end="-->"if curr.next else '')
            curr = curr.next
    
head = Node(10)
head.next = Node(30)
head.next.next = Node(40)

head = Node.deleteLastNode(head)


Node.printList(head) """

# delete a node with only pointer given to it

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

    def deleteNode(node):
        if node is None and node.next is None:
            print("Node cannot be deleted")
            return
        next_node = node.next
        node.key = next_node.key
        node.next = next_node.next
        next_node.next = None

    def printList(head):
        curr = head
        while curr is not None:
            print(curr.key,end='-->'if curr.next else '')
            curr = curr.next

        

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Before deletion:")
Node.printList(head)


Node.deleteNode(head.next.next)

print("\nAfter deletion:")
Node.printList(head)

