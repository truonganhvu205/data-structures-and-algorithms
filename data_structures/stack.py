# LIFO - Last In First Out
from collections import deque

class Stack:
    def __init__(self) -> None:
        self.container = deque()
        
    def push(self, value):
        self.container.append(value)
        
        print(self.container)
    
    def peek(self):
        return self.container[-1]
    
    def delete_one(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.peek())
print(stack.delete_one())
print(stack.size())
print(stack.is_empty())