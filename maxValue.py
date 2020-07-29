# # 최댓값 구하기


# print('세정수를 구합니다.')

# a = int(input('a정수를 입력해주세요.'))
# b = int(input('b정수를 입력해주세요.'))
# c = int(input('c정수를 입력해주세요.')) 

# MaxValue = a
# if b>MaxValue: MaxValue = b
# elif c>MaxValue:Maxvalue = c

# print('최댓값: ',MaxValue)



# A = [1,5,6,8,7,9]

# for i in A:
#     max = 0
#     if max == 0 and i>max:
#         max = i

# for j in A:
#     min = 0
#     if min ==0 and j<min:
#         min = j

# print("최댓값 : ",max)
# print("최솟값 : ",min)

# 1부터 N까지 정수의 합 구하기 1(while문)

# print("1부터 n까지의 정수를 입력해주세요.")
# num = int(input("정수를 입력해주세요"))

# sum = 0
# i = 0
# while i<=num:
#     sum+=i
#     i+=1

# print(f'1부터 {num}까지의 합은 : {sum}입니다')

# 1부터 n까지 정수의 합 구하기 2(for문)

print('a부터 b까지의 숫자의 합을 구하시오')
a = int(input('a의 정수 : '))
b = int(input('b의 정수 : '))

 if a > b:
     a,b = b,a
sum = 0
for i in range(a,b+1):
    sum+=i

print(sum)


