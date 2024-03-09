class Binary_search_tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_search_tree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_search_tree(data)
                
    def in_order_traversal(self):
        lst = []
        
        if self.left:
            lst += self.left.in_order_traversal()
            
        lst.append(self.data)
        
        if self.right:
            lst += self.right.in_order_traversal()
            
        return lst
        
    def search(self, value):
        if value == self.data:
            return True
            
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
                
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            if self.right is None:
                return self.left
            else:
                min_value = self.right.find_min()
                self.data = min_value
                self.right = self.right.delete(min_value)
                
        return self
        
def build_tree(lst):
    root = Binary_search_tree(lst[0])
    
    for i in range(1, len(lst)):
        root.add_child(lst[i])
        
    return root

if __name__ == '__main__':
    binary_search_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    
    print(binary_search_tree.in_order_traversal())
    print(binary_search_tree.search(20))

    binary_search_tree.delete(20)
    
    print('After deleting 20:', binary_search_tree.in_order_traversal())