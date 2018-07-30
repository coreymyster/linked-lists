# Corey Sokol

# Creates the node. Simply takes data passed in and sets the data into the node.
# Also declares what the location of the next node is.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    # Sets the head of the node
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Checks if the list is empty by checking if there is a head
    def isEmpty(self):
        return self.head == None
    
    # Returns the size of the queue. The counter increments as it works
    # through the queue and stops once cuurent becomes None.
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    
    # Creates a new node and adds a new item to the queue. 
    def enqueue(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
 
    # Removes oldest item from the queue. Sets head to the next node after the oldest node to remove
    # the first item in the queue.
    def deque(self):
        self.head = self.head.getNext()
        current = self.head
        previous = None
  
        while current != None:
            previous = current
            current = current.getNext()
    
    # Searches the list for a specific item and returns whether it's found or not. 
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
        

mylist = UnorderedList()

#mylist.enqueue(12)
#mylist.enqueue(25)
#mylist.enqueue(129)
mylist.enqueue(1)
mylist.enqueue(5)
mylist.enqueue(53)
print(mylist.size())
mylist.deque()
print(mylist.size())
print(mylist.search(1))
print(mylist.search(5))
print(mylist.search(53))
mylist.deque()
print(mylist.size())
print(mylist.search(5))
print(mylist.search(53))
