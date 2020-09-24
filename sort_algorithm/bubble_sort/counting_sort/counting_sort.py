# 도수 정렬 알고리즘

from typing import MutableSequence

def fsort(a:MutableSequence, max:int) -> None:
    """도수 정렬(배열 원소값은 0 이상 max 이하)"""
    n = len(a)              # 정렬할 배열 a
    f = [0] * (max + 1)     # 누적 도수 분포표 배열 f
    b = [0] * n             # 작업용 배열 b

    for i in range(n): f[a[i]] +=1                                  # 도수 분포표 만들기
    for i in range(1, max + 1) : f[i] += f[i - 1]                   # 누적 도수 분포표
    for i in range(n-1, -1, -1): f[a[i]] -=1; b[f[a[i]]] = a[i]     # 작업용 배열
    for i in range(n): a[i] = b[i]                                  # 배열 복사하기

def counting_sort(a:MutableSequence) -> None:
    fsort(a, max(a))

if __name__ == '__main__':
    num = int(input('배열의 크기 : '))hh
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
    
    counting_sort(x)
    
    print()
    print()

    print('오름차순 정렬')
    for i in range(num):
        print(f'{x[i]}', end='  ')