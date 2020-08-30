# 스택으로 재귀 함수 구현하기(재귀를 구현)

from FixedStack import FixedStack

def recur(n:int) ->int:

    s = FixedStack(n)

    while True:
        
        if n>0:
            s.push(n)
            n = n -1
            continue

        if not s.is_empty(): # 스택이 비어있지 않다면 
            n=s.pop()
            print(n)
            n = n - 2
            continue
        
        break

x = int(input("정수를 입력 : "))

recur(x)

