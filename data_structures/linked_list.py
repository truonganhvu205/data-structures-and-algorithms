class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
    
class Linked_list():
    def __init__(self) -> None:
        self.head = None
        
    def print_ll(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
            
        print(llstr)
            
    def get_length(self):
        itr = self.head
        count = 0
        
        while itr:
            count += 1
            itr = itr.next
            
        return count
        
    def insert_at_begin(self, data):
        self.head = Node(data, self.head)
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        
        if index == 0:
            self.insert_at_begin(data)
            return
        
        itr = self.head
        count = 0
        
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            
            itr = itr.next
            count += 1
    
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
            
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
    
    def insert_values(self, lst):
        self.head = None
        
        for data in lst:
            self.insert_at_end(data)
            
linked_list = Linked_list()

linked_list.insert_at_begin(0)
linked_list.insert_at_end(1)

linked_list.insert_at(1, 0.5)
linked_list.remove_at(2)

# lst = [1, 2, 3, 4, 5]
# linked_list.insert_values(lst)

linked_list.print_ll()
print(linked_list.get_length())