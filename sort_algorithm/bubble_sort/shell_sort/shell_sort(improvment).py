# 셸 정렬 알고리즘(h * 3 + 1의 수열 사용)

from typing import MutableSequence


def shell_sort2(a:MutableSequence) ->None:
    
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:

        for i in range(h, n):
            j = i - h
            temp = a[i]
            while j >= 0 and a[j] > temp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = temp
        h //= 3


if __name__ == '__main__':
    print(' 쉘 정렬 수행 ')
    num = int(input('배열의 크기 : '))
    arry = [None] * num

    for i in range(num):
        arry[i] = int(input(f'x[{i}] : '))

    shell_sort2(arry)

    print()
    print('오름차순으로 정렬합니다.')
    for i in range(num):
        print(f'arry>[{i}] = {arry[i]}')