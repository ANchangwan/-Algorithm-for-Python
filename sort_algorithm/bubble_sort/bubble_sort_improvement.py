from typing import MutableSequence


# 기본적인 버블정렬
def bubble_sort(data:MutableSequence) -> None:
    """버블정렬"""
    n = len(data)
    for i in range(n - 1):
        for j in range(n-1,i,-1):
            if data[j-1]>data[j]:
                data[j-1],data[j] = data[j], data[j-1]


# 버블 정렬_알고리즘 개선1
def bubble_sort_improvment1(data:MutableSequence) -> None:
    
    n = len(data)
    for i in range(n-1, 0, -1):
        exchange = 0
        for j in range(0, n-1):
            if data[j-1]> data[j]:
                data[j - 1], data[j] = data[j], data[j-1]
                exchange+= 1
        if exchange == 0: # 정렬이 횟수가 0이 되면 정지
            break




# 버블정렬_알고리즘개선2
# 인덱스를 변수에 저장
def bubble_sort_improvment2(data:MutableSequence) -> None:

    n = len(data)
    k = 0
    while k< n-1:
        last = n-1
        for j in range(n-1, k, -1):
            if data[j-1]> data[j]:
                data[j - 1], data[j] = data[j], data[j-1]
                last = j
        k = last