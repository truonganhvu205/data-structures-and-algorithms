# FIFO - First In First Out
from collections import deque

class Queue:
    def __init__(self) -> None:
        self.container = deque()
        
    def push(self, v):
        self.container.appendleft(v)
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