#괄호 문제 풀기 
#괄호쌍 떼어내기 
def dino_parentheses(text) :
    while '()' in text :
        for i in range(len(text) - 1) :
            # 마지막 항목이 여는 괄호이면 오류가 날 수도 있기 때문에 -1
            if text[i] == "(" and text[i + 1] == ")" :
                left = text[:i]
                right = text[i + 2:]
                text = left + right
                # print('s :', text)
                break
    return len(text) == 0

#split()로 한 번에 쌍이 맞는 괄호를 제외해서 나누고,
#.join()을 통해 다시 붙이는 방식 
def dino_parentheses2(text) :
    while '()' in text :
        ts = text.split('()')
        # while 한 번마다 딱 한 번의 split을 사용... 시간이 너무 걸림 
        text = ''.join(ts)
        # print('s :', text)
    return len(text) == 0

# print(dino_parentheses('()((())))'))
# print(dino_parentheses2('()((())))'))
# print(dino_parentheses('()((()))'))
# print(dino_parentheses2('()((()))'))

#스택으로 풀기 
from stack.st1 import Stack1
from datetime import datetime

def solution_dino(txt) :
    st = Stack1(len(txt))
    for i in range(len(txt)) :
        if txt[i] == '(' :
            st.push('(')
        elif txt[i] == ')' :
            if st.empty() :
                return False 
            st.pop()
    return st.empty()
#'('의 갯수로 풀기 
def count_dino(txt) :
    cnt = 0
    for i in range(len(txt)) :
        if txt[i] == '(' :
            cnt += 1
        elif txt[i] == ')' :
            if cnt == 0 :
                return False 
            cnt -= 1
    return cnt == 0

txt = '(' * 10000 + ')' * 10000
start_time = datetime.now()
print(f's_cnt: {len(txt)} result: {dino_parentheses(txt)}')
print('dino_parentheses(txt) :', datetime.now() - start_time)
start_time = datetime.now()
print(f's_cnt: {len(txt)} result: {dino_parentheses2(txt)}')
print('dino_parentheses2(txt) :', datetime.now() - start_time)
start_time = datetime.now()
print(f's_cnt: {len(txt)} result: {solution_dino(txt)}')
print('solution_dino(txt) :', datetime.now() - start_time)
print(f's_cnt: {len(txt)} result: {count_dino(txt)}')
print('count_dino(txt) :', datetime.now() - start_time)

#() {} [] 모두 판단하는 프로그램 만들기 
#짝이 맞는지 확인하는 함수
def is_pair(first, second) :
    if first == '(' and second == ')' :
        return True 
    elif first == '{' and second == '}' :
        return True 
    elif first == '[' and second == ']' :
        return True 
    return False

#peek()와 is_pair()을 사용해서 해당 짝을 만나는 경우, pop()을 통해 제거
def solution_all(txt) :
    st = Stack1(len(txt))
    
    for i in range(len(txt)) :
        if txt[i] in ['(', '{', '['] :
            st.push(txt[i])
        elif is_pair(st.peek(), txt[i]) :
            if st.empty() :
                return False
            st.pop()
    return st.empty()

text = f'{"["*(2*pow(10,4))}{"{"*(2*pow(10,4))}{"("*(2*pow(10,4))}{")"*(2*pow(10,4))}{"}"*(2*pow(10,4))}{"]"*(2*pow(10,4))}'
start_time = datetime.now()
print(f's_cnt: {len(text)} result: {solution_all(text)}')
print('solution_all(text) :', datetime.now() - start_time)