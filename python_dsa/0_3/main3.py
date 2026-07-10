#Queues
#queue is just like waiting lines, whoever first in this one is first

#methods: enqueue, dequeue, peek, isempty
#enqueue = add element at the end
#dequeue = remove element at the front
#peek = first element
#isempty = checks whether it is empty or not


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data) #assign new node element

        if self.rear is None: #if list is empty we assign front and back will be this new node and return
            self.front = self.rear = new_node
            return
        
        #if Linkedlist is not empty
        self.rear.next = new_node   #last element's next pointer stores new node
        self.rear = new_node        #last element will be our new node
    
    def dequeue(self):
        
        if self.front is None: #check if element is empty or not
            print("no element tp delete")
            return
        
        self.front = self.front.next
    
    def peek(self):
        return self.front.data if self.front is not None else None
    
    def isempty(self):
        return True if self.front is None else False
    
    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_queue = Queue()

my_queue.enqueue(10) #stored firstly 
my_queue.enqueue(20)
my_queue.enqueue(30)

my_queue.dequeue() #deletes first one
print(my_queue.peek())

my_queue.display()
