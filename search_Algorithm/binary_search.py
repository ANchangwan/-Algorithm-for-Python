# 이진 검색 알고리즘

from typing import Any,Sequence

def bin_search(a:Sequence, key:Any) ->int:
    
    """시퀀스 a에서 key와 일치하는 원소를 이진검색"""

    front = 0           # 검색범위 맨 앞 원소의 인덱스
    end = len(a) - 1    # 검색범위 맨 끝 원소의 인덱스

    while True:
        middle = (front + end) // 2 # 중앙 원소 인덱스
        if a[middle] == key:
            return middle           # 검색 성공
        elif a[middle] < key:
            front = middle + 1      # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            end = middle - 1        # 검색 범위를 앞쪽 절반으로 좁힘
        if front > end:
            break
    
    return -1


if __name__ == "__main__":
    num = int(input("원소의 크기 : "))
    a = [None]*num

    print('오름차순으로 입력하세요')

    for i in range(num):
        a[i] = int(input(f'원소 a[{i}] : '))
       
    
    key = int(input('찾고싶은 원소 값 : '))

    idx = bin_search(a, key)

    if idx == -1:
        print('찾고자 하는 원소값이 없습니다.')
    else:
        print(f"검색 값 a[{idx}]입니다.(값 : {a[idx]}) ")
