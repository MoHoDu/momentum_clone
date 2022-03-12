class Stack1() :
    arr = []
    last_index = 0
    
    def __init__(self, size=10000) :
        self.arr = [None] * size
    
    def push(self, value) :
        self.arr[self.last_index] = value
        self.last_index += 1
    
    def pop(self) :
        if self.last_index <= 0 :
            # return None  
            raise Exception('Stack is empty')     
         
        value = self.arr[self.last_index - 1]
        self.last_index -= 1
        return value
        
    def empty(self) :
        if self.last_index == 0 :
            return True
        else :
            return False
        
    def peek(self) :
        if self.empty() :
            raise Exception('Stack is empty')
        return self.arr[self.last_index - 1]