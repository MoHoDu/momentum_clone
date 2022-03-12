# open addressing
class HashTable :
	def __init__(self) :
		self.size = 10
		self.table = [0 for _ in range(self.size)]
		
	def hash(self, name) :
		ascii_sum = 0
		for word in name :
			ascii_sum += ord(word)
		return ascii_sum % self.size
		
	def insert(self, name, value) :
		hashIndex = self.hash(name)
		for i in range(hashIndex, hashIndex + self.size) :
			if self.table[i % self.size] == 0 :
				self.table[i] = value
				return
        # 해당 인덱스에 값이 이미 있다면, 다음 인덱스로 선형적으로 이동
        # 하면서 빈 인덱스에 새로운 값을 저장하는 방식 
        # 빈 인덱스가 나오기까지 계속 선형적으로 이동해야 하기 때문에 
        # 비효율적인 시간이 걸릴 수 있고, 그래서 원래 범위의 2배로 배열 
        # 크기를 정해서 빈 인덱스를 충분히 마련해 놓는 편이 좋음
				
	def printTable(self) :
		for idx, value in enumerate(self.table) :
			if value != 0 :
				print([idx, value])
				
table = HashTable()
table.insert('jisoo', 1000)
table.insert('kavin', 2000)
table.insert('sam', 3000)
table.insert('hash kim', 4000)
table.insert('mirror', 5000)
table.printTable()