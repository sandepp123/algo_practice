class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None
        self.prev  = None

    def __str__(self):
        # return f"{str(self.prev)} <-- {str(self.value)} --> {str(self.next)}"
        return str(self.value)
    


class DoubleLinkedList:
    def __init__(self):
        self.head  =  None
        self.tail  =  None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result +=str(temp_node.value)
            if temp_node.next is not None:
                result+= " <--> "
            temp_node = temp_node.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length+=1

    def prepend(self,value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = None
            self.prev = None
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def traverse(self):
        curr_node = self.head
        # result = ""
        while curr_node is not None:
            print(curr_node.value)
            if curr_node.next is  None:
                break
            curr_node = curr_node.next
        return True
    
    def reverse_traverse(self):
        curr_node = self.tail
        index = 0
        while curr_node is not None:
            print(curr_node)
            if curr_node.prev is None:
                # print("ejjejej")
                break
            curr_node = curr_node.prev
        return True
    
    def search(self,value):
        curr_node = self.head
        index = 0
        while curr_node is not None:

            if curr_node.value == value:
                return index

            curr_node = curr_node.next
            index+=1
        return False

    def get(self,index):

        if index<0 or index >= self.length:
            return "Out of bound index"
        curr_node = self.head
        if index < self.length//2:

            for i in range(index):
            
                curr_node = curr_node.next
            return curr_node

        else:
            curr_node = self.tail
            for i in range(self.length-1,index,-1):
                curr_node = curr_node.prev
            return curr_node

    def set(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self,index,value):
        node = self.get(index-1)
        print(node.value)
        if node:

            new_node = Node(value)
            next_node = node.next
            node.next = new_node
            new_node.prev = node
            new_node.next = next_node
            next_node.prev = node

            # node.next = new_node

            return True
        return False 

cl = DoubleLinkedList()
cl.append(10)
cl.append(20)
cl.append(30)
cl.append(40)
cl.append(50)
cl.append(60)
cl.append(70)
cl.append(80)
cl.append(20000)
cl.append(10000)
# print()
# print(cl,"sksksk")
# cl.traverse()
# cl.reverse_traverse()
# print(cl.search(1012))
print(cl.insert(3,1063))
print(cl)
