# 순수한 재귀 함수 

def recur(n:int)->int:
    if n>0:
        recur(n-1)
        print(n)
        recur(n-2)

x = int(input('정숫값을 입력하세요 : '))

recur(x)

# 꼬리 재귀 제거하기

def recur_remove_tail(n:int) ->int :
    while n > 0 :
        recur_remove_tail(n-1)
        print(n)
        n = n - 2

y = int(input('정숫값을 입력하세요 : '))

recur_remove_tail(y)