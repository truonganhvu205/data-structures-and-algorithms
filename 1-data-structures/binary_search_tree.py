class Binary_search_tree:
    def __init__(self, d):
        self.d = d
        self.l = None
        self.r = None

    def add_child(self, d):
        if d == self.d:
            return
        
        if d < self.d:
            if self.l:
                self.l.add_child(d)
            else:
                self.l = Binary_search_tree(d)
        else:
            if self.r:
                self.r.add_child(d)
            else:
                self.r = Binary_search_tree(d)
            
    def in_order_traversal(self):
        e = []

        if self.l:
            e += self.l.in_order_traversal()

        e.append(self.d)

        if self.r:
            e += self.r.in_order_traversal()

        return e
    
    def search(self, v):
        if self.d == v:
            return True
        
        if v < self.d:
            if self.l:
                return self.l.search(v)
            else:
                return False
        else:
            if self.r:
                return self.r.search(v)
            else:
                return False

    def find_min(self):
        if self.l is None:
            return self.d
        else:
            return self.l.find_min()

    def find_max(self):
        if self.r is None:
            return self.d
        else:
            return self.r.find_max()
    
    def delete(self, v):
        if v < self.d:
            if self.l:
                self.l = self.l.delete(v)
        elif v > self.d:
            if self.r:
                self.r = self.r.delete(v)
        else:
            if self.l is None and self.r is None:
                return None
            elif self.l is None:
                return self.r
            elif self.r is None:
                return self.l
            else:
                mv = self.r.find_min()
                self.d = mv
                self.r = self.r.delete(mv)

        return self
    
def build_tree(e):
    r = Binary_search_tree(e[0])

    for i in range(1, len(e)):
        r.add_child(e[i])

    return r

if __name__ == '__main__':
    l = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(l.in_order_traversal())

    print(l.search(20))

    l.delete(20)
    print('After deleting 20:', l.in_order_traversal())