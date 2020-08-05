from maxValueFunc.maxValue1 import maxValue

# 예제1
# 최댓값

# inputNum = 0
# num = []
# max = 0
# wantTocount = int(input('입력하고 싶은 수를 입력해주세요!'))
# for i in range(wantTocount):
#     inputNum = int(input('정수를 입력해주세요.: '))
#     num.append(inputNum)

# for k in num:
#     if max < k:
#         max = k

# print(f'최대값 : {max}')


# 예제2
# 최댓값

# if __name__ == "__main__":
    
#     print('값을 입력해주세요')
#     value = int(input('원소의 갯수를 입력해주세요 : '))
#     x = [None] * value
    
#     for i in range(value):
#         x[i] = int(input(f'x[{i}]의 값을 입력해주세요 : '))
    
#     print(f'최댓값은 {maxValue(x)}입니다.')

# 예제3
# 원솟값을 난수로 생성

# import random

# print('난수를 발생합니다.')
# num = int(input('원소의 크기 : '))
# lo = int(input('시작값 : '))
# hi = int(input('마지막 값 : '))
# x = [None] * num

# for i in range(len(x)):
#     x[i] = random.randint(lo,hi)
#     print(f'x[{i}]의 값은 {x[i]}입니다.')

# print(f' 최댓값은 {maxValue(x)} 입니다.')

# 예제 4
# 원소값 입력받기


# print('원소값을 입력합니다.')
# print('End를 누르면 종료합니다.')

# number = 0
# x = []

# while True:
#     num = input( f' x[{number}]원소 값 :')
#     if num == 'End'or num =='end':
#         break

#     x.append(int(num))
#     number+=1

# print(f'최댓값 {maxValue(x)}')

# 예제5
# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열리스트)

# t = (4, 7, 8, 9, 15.4, 459, 55)
# s = 'String'
# a = ['BTS','윤유선', '창완']

# print(f'최댓값 : {maxValue(t)}')
# print(f'문자열 최댓값 : {maxValue(s)}')
# print(f'문자열 리스트 최댓값 :{maxValue(a)}')


# 예제6
# 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)

x = ['jone', 'meli','somi','changwan','Tom']

# for i in range(len(x)):
#     print(f'x[{i}]의 값 {x[i]}')

# for i, name in enumerate(x):
#     print(f'x[{i}] = {name}')

# for i, name in enumerate(x,0):
#     print(f'x[{i}] = {name}')

# for i in x:
#     print(i)


# 예제7
# 뮤터블시퀀스 원소를 역순을 정렬

from typing import Any, MutableSequence
def reversed_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    x = len(a) # 가독성을 높이기 위해 x변수 값 선언
    for i in range(x//2):
        a[i],a[x-i-1] = a[x-i-1],a[i]
    
    return a

print('원소를 역순으로 정렬합니다.')
countNum = int(input('원소의 갯수를 입력해주세요 : '))
num = [None]*countNum

for i in range(len(num)):
    num[i] = int(input(f'num[{i}] 입력해주세요 : '))

print()
reversed_array(num)
# 원소를 역순으로 정렬합니다.
for i in range(len(num)):
    print(f'num[{i}] = {num[i]}')
