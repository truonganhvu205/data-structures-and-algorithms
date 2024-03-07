# FIFO - First In First Out
from collections import deque

class Queue:
    def __init__(self) -> None:
        self.c = deque()
        
    def push(self, v):
        self.c.appendleft(v)
        print(self.c)
        
    def peek(self):
        return self.c[-1]
    
    def delete_one(self):
        return self.c.pop()
    
    def size(self):
        return len(self.c)
    
    def is_empty(self):
        return len(self.c) == 0
    
q = Queue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print(q.peek())
print(q.delete_one())
print(q.size())
print(q.is_empty())