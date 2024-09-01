class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        
        curr_node = self.head
        result = ""
        while curr_node is not None:
            # print(curr_node)
            result += str(curr_node.value)
            curr_node = curr_node.next
            if curr_node is self.head:
                break
            result+=" -> "
        return result
    
    def append(self, value):
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head

        self.length+=1
            
    
    def prepend(self, value):
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head

        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length+=1



linked_list = CSLinkedList()
linked_list.append(5)
linked_list.append(6)
print(linked_list)
linked_list.prepend(8)
print(linked_list)
linked_list.prepend(10)
print(linked_list)