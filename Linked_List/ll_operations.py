class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__ (self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # Logic: Assign head to temp, traverse all nodes by temp.next till temp is None
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # Logic: Create a new node, if length is 0, assign head and tail to new node, else assign tail.next to new node and update tail to new node. Increment length by 1
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # Logic: If length is 0, return None. If length is 1, assign head and tail to None and decrement length by 1. 
    # Else, traverse the list till the second last node, assign tail to second last node, set tail.next to None 
    # and decrement length by 1. Return the value of popped node.
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            print_pop_value = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return print_pop_value.value
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        print_pop_value = self.tail
        self.tail = temp
        self.tail.next = None
        self.length -= 1
        return print_pop_value.value
    
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            
        
        
    
    
                
my_linked_list = LinkedList(5)
my_linked_list.append(10)
my_linked_list.append(15)
my_linked_list.append(20)

print("Print value of first element: ",my_linked_list.head.value)
print("Print after append: ")
print(my_linked_list.print_list())

pop_value = my_linked_list.pop()
print("Popped element from end: ", pop_value)

print("Print after popping: ")
print(my_linked_list.print_list())

print("Prepend 0 to the linked list")
my_linked_list.prepend(0)

print("Print after prepending: ")
print(my_linked_list.print_list())