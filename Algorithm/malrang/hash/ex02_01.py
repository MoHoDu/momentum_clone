class HashTable:
    def __init__(self) :
        self.size = 10
        self.table = [0 for _ in range(self.size)]

    def hash(self, name) :
        ascii_sum = 0
        for word in name :
            ascii_sum += ord(word)
        return ascii_sum % self.size

    def insert(self, name, value) :
        # self.table[self.hash(name)] = value
        hashIndex = self.hash(name)
        for i in range(hashIndex, hashIndex + self.size) :
            if self.table[i % self.size] == 0 :
                self.table[i % self.size] = value
                return
    
    def search(self, name) :
        return self.table[self.hash(name)]
    
    def remove(self, name) :
        self.table[self.hash(name)] = 0
        
    def printTable(self) :
        for idx, value in enumerate(self.table) :
            if value != 0 :
                print([idx, value])
    
table = HashTable()
table.insert('jisoo', 1000)
table.insert('kavin', 2000)
table.insert('sam', 3000)
table.insert('hash kim', 4000)
table.insert('mirror', 5000) # kavin과 충돌
table.printTable()

print(table.search('jisoo'))
table.remove('jisoo')
table.printTable()