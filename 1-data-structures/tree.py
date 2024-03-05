class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.children = []
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        lvl = 0
        p = self.parent
        
        while p:
            lvl += 1
            p = p.parent
            
        return lvl
    
    def print_tree(self):
        sp = ' ' * self.get_level() * 4
        pf = sp + '|__ ' if self.parent else ''
        
        print(pf + self.data)
        
        if self.children:
            for child in self.children:
                child.print_tree()
                
def build_tree():
    root = Tree('Electronics')
    
    cellphone = Tree('Cellphones')
    cellphone.add_child(Tree('Samsung'))
    cellphone.add_child(Tree('iPhone'))
    
    laptop = Tree('Laptops')
    laptop.add_child(Tree('Dell'))
    laptop.add_child(Tree('Macbook'))
    
    root.add_child(cellphone)
    root.add_child(laptop)
    
    root.print_tree()
    
if __name__ == '__main__':
    build_tree()