# 순차 탐색
def seqsearch (n, S, x):
    location = 1
    while (location <= n and S[location] != x):
        location += 1
    if (location > n) :
        location = 0
    return location

# 합 구하기
S = [0, 10, 7, 11, 5, 13, 8]
x = 5
location = seqsearch(len(S) - 1, S, x)
# pseudo-code를 썼으므로 인덱스 0 값은 제외
print('location =', location)

def sum(n, S):
    result = 0
    for i in range(1, n + 1):
        result += S[i]
    return result

S = [-1, 10, 7, 11, 5, 13, 8]
sum_value = sum(len(S) - 1, S)
print('sum =', sum_value)

# 비내림차순(오름차순) 정렬: 교환 정렬 알고리즘
def exchange(S):
    n = len(S) #실제 n = n-1
    for i in range(n-1): # i부터 n-2까지 (슈도코드 0 빼니까)
        for j in range(i + 1, n): # i+1부터 n-1까지
            if(S[i] > S[j]):
                S[i], S[j] = S[j], S[i] #파이썬에서의 swap
            #     print(S, 'v', S[i])
            # else:
            #     print(S, 'x', S[i])
    return S

S = [-1, 10, 7, 11, 5, 13, 8]

print('Before=', S)
sortedS = exchange(S)
print('After =', sortedS)

#행렬의 곱셈
def matrixmult (A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    print(C)
    # [0] * n = [0 0] 
    # [0 0], [0 0], [0 0]... n번
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                print('i =', i, 'j =', j, 'k =', k)
                print(C)
    return C

A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
print('A =', A)
print('B =', B)
print('C =', matrixmult(A, B))