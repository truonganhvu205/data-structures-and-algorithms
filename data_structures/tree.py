class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.children = []
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level += 1
            p = p.parent
            
        return level
        
    def print_tree(self):
        space = ' ' * self.get_level() * 4
        prefix = space + '|_ ' if self.parent else ''
        
        print(prefix + self.data)
        
        if self.children:
            for child in self.children:
                child.print_tree()
                
def build_tree():
    root = Tree('Electronics')
    
    cellphones = Tree('Cellphones')
    cellphones.add_child(Tree('iPhone'))
    cellphones.add_child(Tree('Samsung'))
    
    laptops = Tree('Laptops')
    laptops.add_child(Tree('Macbook'))
    laptops.add_child(Tree('Dell'))
    
    root.add_child(cellphones)
    root.add_child(laptops)
    
    root.print_tree()
    
if __name__ == '__main__':
    build_tree()