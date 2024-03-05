class Hash_table_collision:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0

        for char in key:
            hash += ord(char)

        return hash % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False

        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True

        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                print('del', index)

                del self.arr[h][index]

hash_table_collision = Hash_table_collision()

print(hash_table_collision.get_hash('march 6'))
print(hash_table_collision.get_hash('march 17'))

hash_table_collision['march 6'] = 0
hash_table_collision['march 7'] = 1
hash_table_collision['march 8'] = 2
hash_table_collision['march 17'] = 3

print(hash_table_collision.arr)

print(hash_table_collision['march 6'])
print(hash_table_collision['march 17'])

del hash_table_collision['march 17']

print(hash_table_collision.arr)