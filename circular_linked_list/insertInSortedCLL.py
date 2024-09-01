import logging
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

        
    def insert_into_sorted(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.tail.next = node
            self.length+=1
            return True
        if self.length == 1:
            if self.head.data < value:
                self.head.next = node
                self.tail = node
                node.next = self.head
                self.length+=1
                return True
            else:
                temp = self.head
                node.next =  temp
                self.head = node
                self.tail = temp
                # self.head = node
                self.tail.next = node
                self.length+=1
                return True
        else:
            
            curr = self.head
            next_node = curr.next
            
            while curr is not None:
                # logging.log(curr.data)
                if self.head.data >= value:
                    # print("here")
                    node.next = self.head
                    self.head = node
                    self.tail.next = node
                    self.length+=1
                    return True

                if curr.data < value and next_node.data>=value and next_node is not self.head:
                    curr.next = node
                    node.next = next_node
                    self.length+=1
                    return True


                curr = curr.next
                next_node = curr.next
                if curr.next is self.head:
                    curr.next = node
                    self.tail = node
                    node.next = self.head
                    self.length+=1
                    return True

                


                    

            


linked_list = CircularLinkedList()
linked_list.append(11)
linked_list.append(22)
linked_list.append(33)
linked_list.append(44)
linked_list.append(55)
linked_list.append(65)
linked_list.print_list()
print(linked_list.is_sorted())
linked_list.insert_into_sorted(62)
linked_list.print_list()


# Example usage
clist = CircularLinkedList()
clist.insert_into_sorted(3)
clist.insert_into_sorted(1)
clist.insert_into_sorted(2)
clist.insert_into_sorted(4)
 
print("The circular linked list is:")
clist.print_list()