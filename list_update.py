# 1부터 n까지 정수의 합 구하기

# def sum_1ton(n):

#     sum = 0
#     while n>0:
#         sum+=n
#         n-=1
#     return sum

# n = int(input('x의 값을 입력하세요.'))
# print(f'1부터 {n}까지 정수의 합은 {sum_1ton(n)}입니다.')

# 인수가 이뮤터블일때
# 함수 안에서 매개변수의 값을 변경하면 다른 객체를 생성하고 그 객체에 대한 참조로 업데이트됩니다.
# 따라서 매개변수의 값을 변경해도 호출하는 쪽의 실제 인수에는 영향을 주지 않습니다.

# 리스트에서 임의의 원솟값을 업데이트하기
def changeList(lst, idx,val):
    """lst[idex]을 val로 업데이트"""
    lst[idx] = val
    


x = [11,22,33,44,55]
print('x=',x)

idx = int(input("인덱스의 위치를 입력하세요"))
val = int(input("바꾸고 싶은 값을 입력하세요."))

changeList(x,idx,val)
print("x=",x)

# 인수가 뮤터블일때 
# 함수 안에서 매개변수의 값을 변경하면 객체 자체를 업데이트합니다.
# 따라서 매개변수의 값을 변경하면 호출하는 쪽의 실제 인수는 값이 변경됩니다.