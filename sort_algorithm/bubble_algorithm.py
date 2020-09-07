from typing import MutableSequence

def bubble_sort(data:MutableSequence) -> None:
    """버블정렬"""
    n = len(data)
    for i in range(n - 1):
        for j in range(n-1,i,-1):
            if data[j-1]>data[j]:
                data[j-1],data[j] = data[j], data[j-1] 


if __name__ == "__main__":
    num = int(input("데이터 수를 입력하세요 : "))
    x = [None] * num # 원소 수가 num인 배열 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))


    bubble_sort(x)

    print("버블 정렬을 수행합니다.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')