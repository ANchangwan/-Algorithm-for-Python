from typing import MutableSequence

def shell_sort(a:MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            temp = a[i]
            while j > 0 and a[j]>temp:
                a[j+h] = a[j]
                j-=h
            a[j + h] = temp
        h // =2

if __name__ == '__main__':
    print(' 쉘 정렬 수행 ')
    num = int(input('배열의 크기 : '))
    arry = [None] * num

    for i in range(num):
        arry[i] = int(input(f'x[{i}] = {x[i]}'))

    shell_sort(arry)

    print()
    print('오름차순으로 정렬합니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

