# 최댓값 구하기


print('세정수를 구합니다.')

a = int(input('a정수를 입력해주세요.'))
b = int(input('b정수를 입력해주세요.'))
c = int(input('c정수를 입력해주세요.')) 

MaxValue = a
if b>MaxValue: MaxValue = b
elif c>MaxValue:Maxvalue = c

print('최댓값: ',MaxValue)



A = [1,5,6,8,7,9]

for i in A:
    max = 0
    if max == 0 and i>max:
        max = i

for j in A:
    min = 0
    if min ==0 and j<min:
        min = j

print("최댓값 : ",max)
print("최솟값 : ",min)


