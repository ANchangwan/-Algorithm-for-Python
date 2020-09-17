# 퀵 정렬 알고리즘 구현

from typing import MutableSequence

def qsort(a:MutableSequence, left:int, right:int) -> None:

   
    start = left
    end = right
    pivot = a[(left + right) // 2]

    print(f'a[{start}] ~ a[{end}] : ',*a[left: right+1])

    while start <= end:
        while a[start]<pivot: start+=1
        while a[end]>pivot: end-=1
        if start <= end:
            a[start], a[end] = a[end], a[start]
            start+=1
            end-=1
        
    if left < end: qsort(a,left,end)
    if start < right : qsort(a,start,right)

def quick_sort(a:MutableSequence) -> None:
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    num = int(input('원소의 크기 : ')) # 원하는 배열의 크기 입력
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] = '))

    quick_sort(x)
    
    print("오름차순정렬")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')