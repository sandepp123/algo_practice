class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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
    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
        curr_node = self.head
        if self.length == 0:
            return False
        if self.length ==1:
            return True
        while curr_node is not None:
            print(curr_node.data,curr_node.next.data)
            if curr_node.data > curr_node.next.data:
                return False
            curr_node = curr_node.next

            if curr_node.next is self.head:
                return True

        


linked_list = CircularLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.print_list()
print(linked_list.is_sorted())