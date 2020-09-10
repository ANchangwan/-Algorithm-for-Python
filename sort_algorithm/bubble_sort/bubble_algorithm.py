from typing import MutableSequence
from bubble_sort_improvement import *

def bubble_sort(data:MutableSequence) -> None:
    """버블정렬"""
    n = len(data)
    for i in range(n - 1):
        for j in range(n-1,i,-1):
            if data[j-1]>data[j]:
                data[j-1],data[j] = data[j], data[j-1]
                

def bubble_sort_verbose(data:MutableSequence) ->None:
    """버블정렬"""
    comparison_cnt = 0 # 비교 횟수
    exchange_cnt = 0   # 교환 횟수
    n = len(data)
    for i in range(n - 1):
        print(f'패스{i + 1}')
        for j in range(n-1,i,-1):
            exchange = 0
            for m in range(0,n-1):
                print(f'{data[m]:2}' + (' ' if m != j -1 else
                                            ' +'if data[j-1]>data[j] else ' -'), 
                                            end= '')
            print(f'{data[n - 1]:2}')
            comparison_cnt+=1
            if data[j-1] > data[j]:
                exchange_cnt+=1
                data[j-1],data[j] = data[j],data[j-1]
                exchange+=1
        if exchange == 0:
            break

        for m in range(0, n-1):
            print(f'{data[m]:2}',end=' ')
        print(f'{data[n-1]:2}')
    print(f'비교를 {comparison_cnt}번 했습니다.')
    print(f'교환을 {exchange_cnt}번 했습니다.')

if __name__ == "__main__":
    num = int(input("데이터 수를 입력하세요 : "))
    x = [None] * num # 원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    print()
    # bubble_sort_verbose(x)
    bubble_sort_improvment2(x)

    print("버블 정렬을 수행합니다.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')