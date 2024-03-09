class Hash_table_collision:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        
        for char in key:
            hash += ord(char)
            
        return hash % self.MAX
        
    def __getitem__(self, key):
        index = self.get_hash(key)
        
        for kv in self.arr[index]:
            if kv[0] == key:
                return kv[1]
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        
        for index, kv in enumerate(self.arr[h]):
            if len(kv) == 2 and kv[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                
        if not found:
            self.arr[h].append((key, value))
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print('del', index)
                del self.arr[h][index]
    
hash_table_collision = Hash_table_collision()

hash_table_collision['march 6'] = 1
hash_table_collision['march 7'] = 2
hash_table_collision['march 8'] = 3
hash_table_collision['march 9'] = 4
hash_table_collision['march 17'] = 5

print(hash_table_collision['march 6'])

hash_table_collision['march 6'] = 1.5

print(hash_table_collision['march 6'])

print(hash_table_collision.arr)

del hash_table_collision['march 17']

print(hash_table_collision.arr)