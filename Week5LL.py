#Weekk5LL - William Croslen

class Node:
    def __init__(self,item=None,next = None):
        self.item = item
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head

    def addLast(self, item):
        temp = Node(item)
        t = self.head
        if self.head == None:
            self.head = Node(item)
            return
        else:
            while t.next is not None:
                t = t.next
            t.next = temp
      
    def addFirst(self, item):
        self.head = Node(item,self.head)
        
    def add(self, index, item): 
        if index <= 0:
            self.head = Node(item,self.head)
            return
        count = 0
        t = self.head
        temp = Node(item)
        while count!=index:
            if(t.next is not None):
                count = count+1
                t = t.next
            else:
                break
        tnex = t.next
        t.next = temp
        temp.next = tnex
        
    def clear(self):
        self.head = None
        
    def contains(self,x):
        if self.head is None:
            print("list is empty")
            return False
        curr = self.head
        while curr is not None:
            if curr.item == x:
                return True
            else:
                curr = curr.next
        return False
         
    
    def getIndexOf(self, item):
        count = 0
        temp = self.head
        while temp.item != item:
            if temp.next is None:
                print("ITEM: ",item," is not in the list")
                return -1
            count = count + 1
            temp = temp.next
        return count
    
    def get(self, index):
        count = 0
        temp = self.head
        if temp is None:
            print("Index: ",index," is not in this list")
            return None
        while count != index:
            if temp.next is None:
                print("Index: ",index," is not in this list")
                return None
            count = count + 1
            temp = temp.next
        return temp.item
    
    def getFirst(self):
        return self.head.item
    
    def getLast(self):
        t = self.head
        if self.head == None:
            return
        else:
            while t.next is not None:
                t = t.next
            return t.item
        
    def remove(self, index):
        if index <= 1:
            return None
        count = 0
        t = self.head
        while count != index-1:
            if(t.next is not None):
                count = count+1
                t = t.next
            else:
                break
        t.next=t.next.next
        
    def removeFirst(self):
        t = self.head
        if self.head == None:
            return
        self.head = t.next
        
    def removeLast(self):
        t = self.head
        while t.next is not None:
            if t.next.next is None:
                t.next = None
                break
            t = t.next
        t = None
        
   
                
    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count = count + 1
            temp = temp.next
            
        return count
    
    def isEmpty(self):
        return self.head is None
    
    def printList(self):
            print("LIST:")
            temp = self.head
            while temp is not None:
                print(temp.item)
                temp = temp.next 
    

ll = SinglyLinkedList()
#ll.append
ll.addFirst(5)
ll.addFirst(4)
ll.addFirst(3)
ll.add(1,1000)
ll.add(1,100)
ll.add(3,7)
ll.add(0,69)
ll.addLast(0)
ll.addLast(9)
print("First", ll.getFirst())
print("Last", ll.getLast())
print("LENGTH",ll.size())
ll.getIndexOf(1)
x=7
print("The Index of", x, "is:",ll.getIndexOf(x))
ll.printList()
print("REMOVE ")
ll.remove(2)
print("GET   ",ll.get(2))
ll.printList()
ll.clear()
ll.get(2)
ll.printList()
ll.addFirst(6868)
ll.addFirst(12)
ll.addFirst(12)
ll.removeFirst()
ll.printList()
ll.addFirst(3)
ll.addLast(7777)
ll.addFirst(2)
ll.addFirst(1)
ll.printList()
ll.removeLast()
ll.printList()
