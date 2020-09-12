# 단순 삽입 정렬 알고리즘

from typing import MutableSequence

def insert_sort(a:MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1,n):
        j = i
        temp = a[i]
        while j > 0 and a[j - 1] > temp:
           a[j] = a[j-1]
           j-=1
        a[j] = temp

if __name__ == '__main__':
    print('단순 삽입 정렬')
    print()
    num = int(input('입력할 원소 갯수 : '))
    value = [None] * num

    for i in range(num):
        value[i] = int(input(f'value[{i}] : '))

    insert_sort(value)

    print()

    print('오름차순 정렬')
    for i in range(num):
        print(f'value[{i}] : {value[i]}')