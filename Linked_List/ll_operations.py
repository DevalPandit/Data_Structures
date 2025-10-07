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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # Logic: Create a new node, if length is 0, assign head and tail to new node, else assign tail.next to new node and update tail to new node. Increment length by 1
    # Time Complexity: O(1)
    # Space Complexity: O(1)
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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
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
    
    # Logic: Create a new node, if length is 0, assign head and tail to new node, 
    # else assign new_node.next to head and update head to new node. Increment length by 1
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    # Logic: If length is 0, return None. If length is 1, assign head and tail to None and decrement length by 1. 
    # Else, assign head to temp, update head to head.next, set temp.next to None and decrement length by 1. 
    # Return the value of popped node.
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_element = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_element.value
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp.value
    
    # Logic: If index is less than 0 or greater than or equal to length, return None.
    # Traverse the list till the index and return the value of that node.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(0, index):
            temp = temp.next
        return temp
    
    
    # Logic: If index is less than 0 or greater than or equal to length, return None.
    # Traverse the list till the index and set the value of that node to given value.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def set_value(self, index, value):
        if index < 0 and index >= self.length:
            return None
        temp = self.head
        for _ in range(0, index):
            temp = temp.next
        temp.value = value
        return True
    
    
    # Logic: Use get method to get the node at the index, if it is not None, set its value to given value.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def set_value_using_get(self, index, value):
        temp_node = self.get(index)
        if temp_node is not None:
            temp_node.value = value
            return True
        return None
                
    # Logic: Create a new node, use get method to get the node at the index and the previous index.
    # If both are not None, set new_node.next to index_node and previous_index_node.next to new_node.
    # Increment length by 1 and return True.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def insert(self, index, value):
        insert_node = Node(value)
        insert_index_node = self.get(index)
        prev_index_node = self.get(index-1)
        if insert_index_node.value is not None and prev_index_node.value is not None:
            insert_node.next = insert_index_node
            prev_index_node.next = insert_node
            self.length += 1
            return True
        return None
    
    # Logic: Use get method to get the node at the index and the previous index.
    # If both are not None, set previous_index_node.next to index_node.next, set index_node.next to None.
    # Decrement length by 1 and return the value of removed node.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def remove(self, index):
        remove_node = self.get(index)
        prev_node_to_remove = self.get(index-1)
        if prev_node_to_remove is None or remove_node is None:
            return None
        prev_node_to_remove.next = remove_node.next
        remove_node.next = None
        self.length -= 1
        return remove_node.value
        
    # Logic: Swap head and tail
    # Traverse the list and for each node, set its next to previous node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

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

pop_first_value = my_linked_list.pop_first()
print("Popped first element: ", pop_first_value)

print("Print after popping first element: ")
print(my_linked_list.print_list())

get_value_at_index_1 = my_linked_list.get(1)
print("Value at index 1: ", get_value_at_index_1.value)

set_value_at_index_1 = my_linked_list.set_value(1, 100)
print("Set value at index 1 to 100: ", set_value_at_index_1)

print("Print after setting value at index 1: ")
print(my_linked_list.print_list())

set_value_at_index_1_using_get = my_linked_list.set_value_using_get(5, 200)
print("Set value at index 5 to 200 using get method: ", set_value_at_index_1_using_get)

print("Print after setting value at index 5 using get method: ")
print(my_linked_list.print_list())


insert_value_at_index_2 = my_linked_list.insert(2, 50)
print("Insert value at index 2: ", insert_value_at_index_2)

print("Print after inserting value at index 2: ")
print(my_linked_list.print_list())

print("Remove value at index 2: ", my_linked_list.remove(2))

print("Print after removing value at index 2: ")
print(my_linked_list.print_list())

print("Reverse the linked list: ", my_linked_list.reverse())
print("Print after reversing the linked list: ")
print(my_linked_list.print_list())