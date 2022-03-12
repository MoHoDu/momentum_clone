import sys 

stack = []
cnt = int(sys.stdin.readline())
for N in range(cnt) :
    ans = sys.stdin.readline().split()
    order = ans[0]
    if order == 'push' :
        value = ans[1]
        stack.append(value)
    elif order == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif order == 'size' :
        print(len(stack))
    elif order == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif order == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
