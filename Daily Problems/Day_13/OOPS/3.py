
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addLast(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def addFirst(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first = Node(value)
            first.next = self.head
            self.head = first

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")

    def length(self):
        len = 0
        current = self.head
        if current is None:
            return 0
        while current is not None:
           len +=1
           current = current.next
        return len


    def add(self,index,value):
        current = self.head
        index_count = 0
        if index ==0:
            self.addFirst(value)
        if index == self.length():
            self.addLast(value)
        while current is not None:
            if index_count == index-1:
                new = Node(value)
                new.next = current.next
                current.next = new
                break
            index_count += 1

        self.traverse()

    def removeFirst(self):
        if self.head == None:
            return "Linklist is empty"
        elif self.head.next == Node :
            self.head = None
            return "Linklist has become empty"
        else:
            first = self.head.next
            self.head = first
            return self.traverse()

    def removeLast(self):
        if self.tail == None:
            return "Linklist is empty"
        elif self.tail.next == Node :
            self.tail = None
            return "Linklist has become empty"       
        else:
            self.remove(self.length()-1)
            
    def remove(self,index):
        current = self.head
        index_count = 0
        if index ==0:
            self.removeFirst()
            return self.traverse()
        while current is not None:
            if index_count == index-1:
                to_remove = current.next
                current.next = to_remove.next
                to_remove.next = None
                break
            index_count += 1
            current = current.next

        self.traverse()

        


l1 = LinkList()

l1.addFirst(10)
l1.addFirst(20)
l1.addLast(30)
l1.addFirst(40)
l1.add(1,100)
print(l1.length())
l1.removeLast()

# l1.traverse()

