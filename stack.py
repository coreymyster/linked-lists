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
    def __init__(self):
        # Sets the head of the node
        self.head = None
    
    # Checks if the list is empty by checking if there is a head
    def isEmpty(self):
        return self.head == None
    
    # Creates a new node for each item passed in and sets it as the new head
    def push(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    # Traverses the node to check how many items there are.
    # An external reference 'count' counts how many times the loop is run to return number of items.
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    
    # Searches for a specific item in each node.
    # If the current node data = item passed in then return true.
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    # Removes last item passed in since this is a stack (LIFO).
    # Move the head to the next node, effectively removing the previous from the list.
    def pop(self):
        current = self.head
        previous = None
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    
# Creates an empty unordered list
mylist = UnorderedList()

# Adds to the list, checks it's size, removes items and searches for items.
mylist.push(80)
print(mylist.size())
mylist.push(3)
mylist.push(67)
mylist.push(15)
print(mylist.size())
print(mylist.search(15))

mylist.pop()
print(mylist.size())
print(mylist.search(15))
mylist.push(15)
print(mylist.size())