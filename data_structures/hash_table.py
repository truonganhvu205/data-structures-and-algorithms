class Hash_table:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        
        for char in key:
            hash += ord(char)
            
        return hash % self.MAX
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        
        return self.arr[h]
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
hash_table = Hash_table()

hash_table['march 6'] = 0
hash_table['march 7'] = 1

print(hash_table.arr)
print(hash_table['march 6'])

del hash_table['march 7']

print(hash_table['march 7'])