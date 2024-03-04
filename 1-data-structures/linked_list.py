class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self) -> None:
        self.h = None
        
    def print_ll(self):
        if self.h is None:
            print('Linked list is empty')
            return
        
        i = self.h
        ll = ''
        
        while i:
            ll += str(i.data) + ' --> ' if i.next else str(i.data)
            i = i.next
            
        print(ll)
        
    def get_length(self):
        i = self.h
        c = 0
        
        while i:
            c += 1
            i = i.next
            
        return c
    
    def insert_at_begin(self, d):
        self.h = Node(d, self.h)
        
    def insert_at_end(self, d):
        if self.h is None:
            self.h = Node(d, None)
            return
        
        i = self.h
        
        while i.next:
            i = i.next
            
        i.next = Node(d, None)
        
    def insert_at(self, id, d):
        if id < 0 or id > self.get_length():
            raise Exception('Invalid index')
        
        if id == 0:
            self.insert_at_begin(d)
            return
        
        i = self.h
        c = 0
        
        while i:
            if c == id - 1:
                i.next = Node(d, i.next)
                break
            
            i = i.next
            c += 1
            
    def remove_at(self, id):
        if id < 0 or id > self.get_length():
            raise Exception('Invalid index')
        
        if id == 0:
            self.h = self.h.next
            return
        
        i = self.h
        c = 0
        
        while i:
            if c == id - 1:
                i.next = i.next.next
                break
            
            i = i.next
            c += 1
            
    def insert_values(self, l):
        self.h = None
        
        for d in l:
            self.insert_at_end(d)

ll = Linked_list()

ll.insert_at_begin(0)
ll.insert_at_end(1)

ll.insert_at(1, 0.5)
ll.remove_at(1)

l = [1, 2, 3, 4, 5]
ll.insert_values(l)

ll.print_ll()
print(ll.get_length())