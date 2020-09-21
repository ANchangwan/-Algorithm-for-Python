# 병합 정렬 알고리즘 
from typing import MutableSequence
def MergeSort(a:MutableSequence) ->None:
    """병합정렬"""
    def _merge_sort(a:MutableSequence, left:int, right:int) -> None:

        if left < right:
            center = (left + right) // 2

            _merge_sort(a,left,center)
            _merge_sort(a,center+1,right)

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p+=1
                i+=1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j+=1

                else:
                    a[k] = a[i]
                    i+=1
                k+=1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
        
    n = len(a)
    buff = [None] * n
    _merge_sort(a,0,n-1)
    del buff  


if __name__ == '__main__':
    num = int(input('배열의 크기 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    MergeSort(x)

    for i in range(num):
        print(f'{x[i]}',end=' ')