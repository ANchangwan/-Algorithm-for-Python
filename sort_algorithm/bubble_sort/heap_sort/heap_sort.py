# 힙 정렬 
from typing import MutableSequence

def heap_sort_(a:MutableSequence) -> None:
    """힙 정렬"""
    def down_heap(a:MutableSequence, left:int, right:int) -> None:
        temp = a[left]

        parent = left
        while parent < (right+1) // 2: # (right+1) //2
            left_reap = parent * 2 +1        # 왼쪽
            right_reap = left_reap + 1      # 오른쪽 자식
            child = right_reap if right_reap <= right and a[right_reap] > a[left_reap] else left_reap
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n-1) // 2, -1, -1):
        down_heap(a,i,n-1)

    for i in range(n-1,0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a,0,i-1)
            
if __name__ == '__main__':
    num = int(input("원하는 배열의 크기 입력 : "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort_(x)

    print('오름차순 정렬')
    for i in range(num):
        print(f'{x[i]}', end = '    ')
