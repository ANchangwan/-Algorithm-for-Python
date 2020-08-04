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
def maxValue(a):

    max = a[0]
    for i in range(0,len(a)):
        if a[i]>max:
            max = a[i]
    
    return max
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


print('원소값을 입력합니다.')
print('End를 누르면 종료합니다.')

number = 0
x = []

while True:
    num = input( '원소 값 :')
    if num == 'End':
        break

    x.append(int(num))
    number+=1

print(f'최댓값 {maxValue(x)}')