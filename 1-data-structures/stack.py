# LIFO - Last In First Out
from collections import deque

class Stack:
    def __init__(self) -> None:
        self.container = deque()
        
    def push(self, v):
        self.container.append(v)
        print(self.container)
    
    def peek(self):
        return self.container[-1]
    
    def delete_one(self):
        self.container.pop()
        return self.container
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
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