#linked list implementation in python
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    #head and data -> next and data -> next and data
    def __init__ (self):
        self.head = None#list starts empty
        self.prev = None
    
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
        new_node.prev = current
    
    def prepend(self, data):
        #new node created
        new_node = Node(data)

        #if list is empty
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head #new node will point to the head
        self.head.prev = new_node #head will point to the new node
        self.head = new_node #head will point to the new node


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

    def reverse(self):
        #reversing the linked list
        current = self.head
        prev_node = None

        #while current checks every node in the list until it reaches the end
        while current:#reach the end of the list
            #store the next node before changing the links
            next_node = current.next
            #reverse the links
            current.next = prev_node
            current.prev = next_node
            #update the previous node to the current node
            prev_node = current
            current = next_node

        #update the head to the last node
        self.head = prev_node
    
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data if slow else None
    

    def check(self, number):
        current = self.head
        a = False
        while current:
            if current.data == number:
                return True
            current = current.next
        return a

    def clear(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.prepend(5)

my_list.display()
my_list.reverse()
my_list.display()
print("Middle element:", my_list.find_middle())

print(my_list.check(10))
my_list.clear()
my_list.display()
my_list.append(23)
my_list.display()