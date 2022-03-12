import sys

st = []
cnt = int(sys.stdin.readline())
for K in range(cnt) :
    value = int(sys.stdin.readline())
    if value == 0 :
        st.pop()
    else :
        st.append(value)
print(sum(st))