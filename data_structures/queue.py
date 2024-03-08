# FIFO - First In First Out
from collections import deque

class Queue:
    def __init__(self) -> None:
        self.container = deque()
        
    def push(self, value):
        self.container.appendleft(value)
        
        print(self.container)
        
    def peek(self):
        return self.container[-1]
    
    def delete_one(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)

print(queue.peek())
print(queue.delete_one())
print(queue.size())
print(queue.is_empty())