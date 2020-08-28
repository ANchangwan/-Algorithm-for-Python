# 양의 정수 n의 팩토리얼 구하기
import math

def fatorial(n:int) ->int:
    if n>0:
        return n * fatorial(n-1)
    else:
        return 1


if __name__ == "__main__":
    n = int(input("값을 입력하세요 : "))
    # print(F'{n}의 팩토리얼 {fatorial(n)}')
    print(math.fatorial(n))