class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0

    def __str__(self):
        temp_node = self.head
        result =  ''
        while temp_node is not None:
            result+=str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' --> '
        return result 
    def append(self,value):

        if self.length==0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node

        else:
            new_node = Node(value)
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.length ==0 :
            self.head = new_node
            self.tail  = new_node
            new_node.next = new_node
        else:
            # new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length+=1


    def insert(self,value,index):
        if index <0 or index>self.length:
            raise Exception("Index out of range")
        
        new_node = Node(value)

        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.tail.next = new_node
                self.head = new_node
        else:
            temp_node = self.head
            for  i in range(index-1):
                temp_node = temp_node.next
            
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length+=1

    def traverse(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next

            if curr_node is self.head:
                break
        
    def search(self,value):
        curr_node = self.head
        found = 0
        for _ in range(self.length):
            if curr_node.value == value:
                print("the element is found at {_}",_)
                found+=1
            curr_node = curr_node.next
        if found==0:
            print("the value is not found")


    def get(self,index):
        if index <0 or index >self.length:
            print("index out of range")
        
        else:
            curr_node = self.head
            for ind in range(index):
                curr_node = curr_node.next
            
            print(curr_node.value)

    def set(self,index, value):
        new_node = Node(value=value)
        if index == -1:
            new_node.next = self.tail
            self.tail     = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        elif index <0 or index >self.length:
            print("index out of range")
        
        else:
            curr_node = self.head
            for ind in range(index-1):
                curr_node = curr_node.next
            
            new_node.next = curr_node.next
            curr_node.next = new_node


    def pop_first(self):
        if self.length == 0 :
            return None
        poped_node = self.head
        if self.length ==1:
            self.head = None
            self.tail = None
            self.tail.next = self.head
        else:
            self.head = self.head.next
            self.tail.next = self.head
            poped_node.next = None
        self.length-=1
        return poped_node
    def pop_last(self):
        if self.length == 0 :
            return None
        popped_node = self.tail
        if self.length ==1:
            self.head = None
            self.tail = None
            self.tail.next = self.head
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            
            popped_node = self.tail
            temp_node.next = self.head
            self.tail = temp_node
        popped_node.next = None
        self.length-=1
        return popped_node 

            



linked_list = CircularLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.prepend(40)
print(linked_list)
linked_list.insert(50,0)
print(linked_list)
linked_list.insert(23,2)
print(linked_list)
linked_list.insert(50-4,4)
print(linked_list)
linked_list.insert(22,2)
print(linked_list)
linked_list.insert(51,0)
print(linked_list)

linked_list.traverse()
linked_list.search(27)
linked_list.get(4)
linked_list.set(4,96)
print(linked_list)
# linked_list.set(0,33)
print(linked_list,"sksksk")
linked_list.pop()
print(linked_list)