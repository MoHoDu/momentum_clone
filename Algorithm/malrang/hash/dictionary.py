# 완주하지 못한 선수 찾기 
joined = ['cat', 'dog', 'elephant', 'lion',
          'leopard', 'zebra', 'horse', 'bear']
passed = ['cat', 'dog', 'elephant', 'lion',
          'leopard', 'zebra', 'horse']

# dictionary
data = {}
for x in joined :
    data[x] = data.get(x, 0)
    # data['동물 이름'] 의 값에 
    # data.get(x, 0) : data[x]가 있으면 해당 value를
    # 없다면, 0을 집어넣음
    data[x] += 1
    # 이후에 1을 더함 (동명이인이 있으면 2가 됨)

for x in passed :
    data[x] -= 1
    # 통과한 선수들의 값들만 1씩 내리면 패스하지 못한 선수만 
    # 0의 값을 가지게 됨 (동명이인의 경우도 두 명 다 통과해야
    # 0의 값을 가질 것임)

answer_list = [k for k, v in data.items() if v > 0]
answer = answer_list[0]
print(answer)