class HashTable :
    def __init__(self) :
        self.size = 10
        self.table = [[]for _ in range(self.size)]
        
    def hash(self, name) :
        ascii_sum = 0
        for word in name :
            ascii_sum += ord(word)
        return ascii_sum % self.size
    
    def insert(self, name, value) :
        hashIndex = self.hash(name)
        self.table[hashIndex].append([name, value])
    # 인덱스에 값을 애초에 [이름, 값]으로 넣는다
    # 이후, 새로운 insert에서 해당 인덱스에 이미 값이 있다면, 
    # 해당 인덱스 배열 뒤로 [새 이름, 새 값]을 넣는다.
    
    def search(self, name) :
        hashIndex = self.hash(name)
        for i in range(len(self.table[hashIndex])) :
            if self.table[hashIndex][i][0] == name :
                print(f"name : {name} / value : {self.table[hashIndex][i][1]}")
                return True
    # search나 remove, update 시에는 hash로 해당 인덱스
    # 값을 알아낸 다음, 해시 테이블[해당 인덱스][0]의 이름 중
    # 원하는 이름과 맞다면, 해당하는 [이름, 값]을 조정한다.

    def remove(self, name) :
        hashIndex = self.hash(name) 
        for i in range(len(self.table[hashIndex])) :
            if self.table[hashIndex][i][0] == name :
                del self.table[hashIndex][i]

    def update(self, name, value) :
        hashIndex = self.hash(name)
        for i in range(len(self.table[hashIndex])) :
            if self.table[hashIndex][i][0] == name :
                self.table[hashIndex][i][1] = value

    def printTable(self) :
        for idx, value in enumerate(self.table) :
            print([idx, value])
    
table = HashTable()
table.insert('jisoo', 1000)
table.insert('kavin', 2000)
table.insert('sam', 3000)
table.insert('hash kim', 4000)
table.insert('mirror', 5000)

table.search('sam')
table.search('hash kim')
table.search('mirror')

table.remove('mirror')
table.printTable()

table.search('hash kim')
table.update('hash kim', 1500)
table.search('hash kim')