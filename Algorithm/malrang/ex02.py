#스택
#스택 구현하기 
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
        
st = Stack1()
print(st.empty())
print(st.arr[:10])
st.push(29)
print(st.empty())
print(st.peek())
print(st.arr[:10])
print(st.pop())
print(st.arr[:10])
print(st.peek())