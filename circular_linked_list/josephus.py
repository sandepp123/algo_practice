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


    def count_nodes(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next
    def josephus_circle(self, step):
        temp = self.head
        while self.count_nodes()!=1:
            for i in range(step-1):

                temp = temp.next
            to_be_deleted = temp
            self.delete_node(to_be_deleted.data)
            temp = temp.next
            # print(self.print_list(),"qkqkqk",self.count_nodes())
        


        return f"Last person left standing: {temp.data}"
    

ll = CircularLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print_list()
print(ll.josephus_circle(2))
