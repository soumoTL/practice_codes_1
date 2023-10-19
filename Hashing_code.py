class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return


hash_table = HashTable(10)


hash_table.insert("apple", 5)
hash_table.insert("banana", 3)
hash_table.insert("cherry", 8)


print("Value for 'apple':", hash_table.search("apple"))
print("Value for 'grape':", hash_table.search("grape"))  


hash_table.delete("banana")

print("Value for 'banana':", hash_table.search("banana")) 
