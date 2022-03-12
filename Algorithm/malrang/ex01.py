#최댓값
from numpy import size


def max_value(list) :
    result = list[0]
    for index in range(1, len(list)) :
        if result < list[index] :
            result = list[index]
    return result 

numbers = [-1, 3, 40, 23, 85, 21, 105, 99]
print("max value =", max_value(numbers))

#최솟값 
def min_value(list) :
    result = list[0]
    for index in range(1, len(list)) :
        if result > list[index] :
            result = list[index]
    return result

print("min value =", min_value(numbers))

#무차별 대입법 
#브루트 포스 - 비밀번호 맞추기 
def decipher(pw) :
    result = 0000
    # i j k l
    for i in range(0, 10) :
        for j in range(0, 10) :
            for k in range(0, 10) :
                for l in range(0, 10) :
                    result = f'{i}{j}{k}{l}'
                    if str(pw) == result :
                        return result
                    else :
                        print("wrong number :", result)

print("password =", decipher('0001'))