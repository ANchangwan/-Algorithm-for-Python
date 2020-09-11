# 단순 선택 정렬
# 안정적이지 않은 정렬, 이웃한 값 끼리 정렬을 수행하는게 아니기 때문에 안정적이지 않다.
from typing import MutableSequence

def selection_sort(a:MutableSequence) ->None:
    """선택 정렬"""
    n = len(a)

    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[j] < a[min]:
              min = j
        
        a[i], a[min] = a[min],a[i]