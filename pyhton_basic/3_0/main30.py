#linked list implementation in python
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None


class LinkedList:
    #head and data -> next and data -> next and data
    def __init__ (self):
        self.head = None#list starts empty
    
    def append(self, data):
        #new node creation
        new_node = Node(data)

        #if list is empty
        if self.head is None:
            self.head = new_node
            return

        #travel to the end of the list
        current = self.head
        while current.next:
            current = current.next
        
        #and append the new node
        current.next = new_node
    
    def prepend(self, data):
        #new node created
        new_node = Node(data)

        #new first node will hold ponter of the old head
        new_node.next = self.head
        #linked list's head will be head
        self.head = new_node
        #new node's given data
        new_node.data = data

    def leng(self):
        current = self.head
        a = 0 #reason for this is we just declare empty node so it will be first node, num of nodes = 1
        while current: #current is used for traveling to the end if the list complexity is O(n)
            a += 1
            current = current.next
        print(a)

    def delete(self, value):
        if self.head is None: #if list is empty
            return
        
        if self.head.data == value: #if the head node is to be deleted
            self.head = self.head.next #head will point to the next node
            return
        
        current = self.head

        while current.next: #loop will run until the last node
            if current.next.data == value: #check
                #current.next will point to the next node of the node to be deleted

                #assining the next of the current node to the next of the node to be deleted
                current.next = current.next.next 
                #returning from the function after deleting the node
                return
            
            current = current.next #jumps to the next node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.prepend(34)
my_list.append(50)
my_list.prepend(23)
my_list.leng()
#23 -> 34 -> 10 -> 20 -> 50 -> None
my_list.delete(10)
my_list.display()
# 23 -> 34 -> 20 -> 50 -> None