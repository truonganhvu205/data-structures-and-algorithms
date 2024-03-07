class Tree:
    def __init__(self, d) -> None:
        self.d = d
        self.p = None
        self.c = []
        
    def add_child(self, ch):
        ch.p = self
        self.c.append(ch)
        
    def get_level(self):
        lvl = 0
        pr = self.p
        
        while pr:
            lvl += 1
            pr = pr.p
            
        return lvl
    
    def print_tree(self):
        sp = ' ' * self.get_level() * 4
        pf = sp + '|__' if self.p else ''
        
        print(pf + self.d)
        
        if self.c:
            for ch in self.c:
                ch.print_tree()
                
def build_tree():
    r = Tree('Electronics')
    
    cp = Tree('Cellphones')
    cp.add_child(Tree('Samsung'))
    cp.add_child(Tree('iPhone'))
    
    lt = Tree('Laptops')
    lt.add_child(Tree('Dell'))
    lt.add_child(Tree('Macbook'))
    
    r.add_child(cp)
    r.add_child(lt)
    
    r.print_tree()
    
if __name__ == '__main__':
    build_tree()