# 세이커 정렬 알고리즘 

from typing import MutableSequence

def shaker_sort(data:MutableSequence) -> None:

    left = 0
    right = len(data)-1
    last = right

    while left < right:
        for j in range(right, left, -1):
            if data[j-1]> data[j]:
                data[j-1], data[j] > data[j], data[j -1]
                last = j
        left = last
    
    for i in range(left, right):
        if data[j-1]> data[j]:
            data[j-1], data[j] > data[j], data[j -1]
            last = j
        right = last