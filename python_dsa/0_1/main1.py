#Stacks in python
#operations: push, pop, peek, isEmpty, size

#push = add element at the top of the stack
#pop = remove the top element of the stack
#peek = return the top element of the stack without removing it
#is_Empty = check if the stack is empty
#size = return the number of elements in the stack

#We can create stack in two ways: list and Linkedlist

#head of the linked list will be top of the stack. stack = pile of plates

#part of the chain = Node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    #add element
    def push(self, data):
        new_node = Node(data) #assign new nodes data
        new_node.next = self.top #new nodes next pointer will be current head(top) node
        self.top = new_node #head(top) of the node will be new node

    def pop(self): #next node will be head(top) node
        if self.top is None:
            return
        self.top = self.top.next

    def peek(self): #returns top element's data
        return self.top.data if self.top != None else None
    
    def isEmpty(self): #returns whether stack is empty or not
        return False if self.top != None else True
    
    def size(self):
        current = self.top
        a = 0
        while current:
            a += 1
            current = current.next
        return a
    
    def display(self):
        current = self.top

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)

my_stack.pop()
my_stack.pop()



my_stack.display()

def reverse_string(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    
    reversed_text = ""
    while not stack.isEmpty():
        reversed_text += stack.peek()
        stack.pop()
    
    return reversed_text


print(reverse_string("bruh it is me"))