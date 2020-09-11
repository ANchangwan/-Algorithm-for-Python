# 세이커 정렬 알고리즘 

from typing import MutableSequence

def shaker_sort(data:MutableSequence) -> None:

    left = 0
    right = len(data)-1
    last = right

    # 뒤에서 sort 수행
    while left < right:
        for j in range(right, left, -1):
            if data[j-1]> data[j]:
                data[j-1], data[j] > data[j], data[j -1]
                last = j
        left = last
    # 앞으로 sort 수행
    for i in range(left, right):
        if data[j-1]> data[j]:
            data[j-1], data[j] > data[j], data[j -1]
            last = j
        right = last

    # 앞뒤로 정렬 수행해서 더 빠른 정렬을 수행