# 배열을 두 그룹으로 나누기
from typing import MutableSequence

def partiction(a : MutableSequence) -> None:
    n = len(a)
    start = 0
    end = n -1
    pivot = a[n // 2]

    while start <= end:
        while a[start] < pivot : start+=1
        while a[end] > pivot : end-=1
        if start <= end:
            a[start], a[end] = a[end], a[start]
            start+=1
            end-=1

    print(f'피벗은 {pivot}입니다.')

    print('피벗 이하 그룹')
    print(*a[0 : start])

    if start > end + 1:
        print(f'피벗값 = {a[end+1 : start]}')

    print('피벗 이상인 그룹')
    print(*a[end + 1:n])


if __name__ == '__main__':
    num = int(input('원소의 크기 : ')) # 원하는 배열의 크기 입력
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] = '))

    partiction(x)