# LIFO - Last In First Out
from collections import deque

class Stack:
    def __init__(self) -> None:
        self.c = deque()
        
    def push(self, v):
        self.c.append(v)
        print(self.c)
    
    def peek(self):
        return self.c[-1]
    
    def delete_one(self):
        return self.c.pop()
    
    def size(self):
        return len(self.c)
    
    def is_empty(self):
        return len(self.c) == 0
    
s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.peek())
print(s.delete_one())
print(s.size())
print(s.is_empty())