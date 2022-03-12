import hashlib

name = 'Mohosung'
result1 = hash(name)
name = name.encode('utf-8')
result2 = hashlib.md5(name)
print(f'hash : ${result1}')
print(f'hashlib.md5 : ${result2.hexdigest()}')
# utf8로 인코딩 후 hashlib.md5로 16진수의 해쉬값 생성
