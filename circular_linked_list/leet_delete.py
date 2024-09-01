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
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        if self.length == 0 :
            return False
        
        if self.length == 1 and self.head.value ==value:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        
        prev = None
        curr_node = self.head

        while True:
            if curr_node.value == value:
                if curr_node == self.head:
                    deleted_node = curr_node
                    self.head = curr_node.next
                    self.tail.next = self.head
                
                else:
                    prev.next = curr_node.next
                    if curr_node is self.tail:
                        self.tail = prev
                
                self.length-=1
                return True
            
            prev = curr_node
            curr_node = curr_node.next
            if curr_node==self.head:
                break
        return False
                

    def count_nodes(self):


        
        count = 0
        curr_node = self.head
        while curr_node is not None:
            count+=1
            curr_node = curr_node.next

            if curr_node is  self.head:
                break
               
        return count






linked_list = CSLinkedList()
linked_list.append(51)
linked_list.append(62)
linked_list.append(54)
linked_list.append(65)
linked_list.append(56)
linked_list.append(67)
linked_list.append(58)
linked_list.append(69)
linked_list.append(501)
linked_list.append(621)
print(linked_list)

print(linked_list.count_nodes())