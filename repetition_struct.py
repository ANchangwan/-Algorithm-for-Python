# # 예제 1(while 문)
# num = int(input('1부터 n까지 합을 구하시오'))
# sum =0
# i = 1
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)
# # 예제 2(for 문)
# n = int(input('1부터 n까지의 정수를 입력해주세요'))
# sum = 0
# for i in range(1,n+1):
#     sum+=i

# print(sum)

# # 예제 3
# print('a부터 b까지의 합을 구합니다.')
# a = int(input('a의 값 : '))
# b = int(input('b의 값 : '))

# if a > b:
#     a,b = b,a
# sum = 0
#  for i in range(a, b+1):
#      sum += i
#  print(sum)

# # 예제 4
# print('a부터 b까지의 합을 구합니다.')
# a = int(input('a의 값 : '))
# b = int(input('b의 값 : '))

# if a > b:
#     a,b = b,a
# sum = 0
# for i in range(a,b+1):
#     if i<b:
#         print(f'{i}+ ',end = '')
#     else:
#         print(f'{i} =', end = '')
#     sum += i

# print(sum)

# 예제 5 (예제 4 개선)

print('a부터 b까지의 합을 구합니다.')
a = int(input('a의 값 : '))
b = int(input('b의 값 : '))

if a<b:
    temp = a
    a = b
    b = temp

sum = 0

for i in range(a, b):
    print(f'{i}+ ',end = '')
    sum+=i

print(f'{b} = ', end ='')
sum+=b
print(sum)

# 효율적인 이유는 조건문을 통해서 크거나 같음을 판별할필요도 없고 반복 횟수를 한번 줄이기 때문에 효율적이다.