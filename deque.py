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
    # Sets the head and tail of the node to keep track of the front and end of the list
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Checks if the list is empty by checking if there is a head
    def isEmpty():
        return self.head == None
    
    # Adds an item to the front of the list. A head tracks the first item added and
    # the tail tracks the most recent item added.
    def addFront(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
    
    # Removes the most recent item from the front of the list.
    # If the next item is None then the item before will be removed.
    def removeFront(self):
        current = self.head
        previous = None
        while current != None:
            if current.getNext() != None:
                previous = current
                current = current.getNext()
            else:
                previous.next = None
                current = None
    
    # Adds a new item to the rear of the list. Similar to a stack, the rear half of the list follows a LIFO structure.
    def addRear(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    # Removes the most recently added item in the rear of the list. 
    def removeRear(self):
        current = self.head
        previous = None
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
     
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
    
    # Returns the size of the deque. The counter increments as it works
    # through the queue and stops once current becomes None.
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

print("Testing the front of the list")
myList = UnorderedList()
myList.addFront(2)
myList.addFront(10)
myList.addFront(7)
myList.addFront(8)
print(myList.size())
print(myList.search(8))
myList.removeFront()
print(myList.size())
print(myList.search(8))
print("--------")
print("Testing the rear of the list")
myList.addRear(5)
myList.addRear(10)
myList.addRear(1)
print(myList.size())
myList.removeRear()
print(myList.size())
print(myList.search(1))
print(myList.search(5))