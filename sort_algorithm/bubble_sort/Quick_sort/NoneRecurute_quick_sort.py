# 비재귀적인 퀵정렬

from stack import Stack
from typing import MutableSequence

def qsort(data:MutableSequence, left:int, right:int) -> None:

    range = Stack(right - left + 1)

    range.push((left,right))

    while not range.is_empty():
        start, end = left, right = range.pop() # 왼쪽, 오른쪽 커서를 꺼냄
        x = data[(left + right) // 2] # (피벗 가운데 원소)

        while start <= end:
            while data[start] < x: start+=1
            while data[end] > x : end-=1
            if start <= end:
                data[start], data[end] == data[end], data[start]
                start += 1
                end -= 1
    
        if left < end: range.push((left, end))
        if start < right: range.push(start, right)