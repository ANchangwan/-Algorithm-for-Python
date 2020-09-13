# 이진 삽입 정렬
# 단순 삽입 정렬은 크기가 커지면 비용이 같이 커져 부담이 커진다. 이진 삽입 정렬은 그 비용은 개선할 수 있다


from typing import MutableSequence
import bisect

def binary_insertion_sort(a : MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        front = 0                   # 검색 범위 앞 원소 인덱스
        end = i -1                  # 검색 범위 뒤 원소 인덱스

        while True:
            middle = (front + end) // 2         # 검색 원소의 중간 원소 인덱스
            if a[middle] == key:                # 검색성공
                break
            elif a[middle]< key:                
                front = middle + 1              # 검색 범위를 뒤쪽 절반으로 좁힘
            else:
                end = middle - 1                # 검색 범위를 앞쪽 절반으로 좁힘
            if front > end:
                break
            
       

        idx = middle +1 if front <= end else end + 1        # 삽입해야 할 위치의 인덱스

        for j in range(i,idx,-1):
            a[j] = a[j-1]
        a[idx] = key


def binary_insertion_sort2(a:MutableSequence) -> None:
    """이진 삽입 정렬(biserct.insort)""" # 표준 라이브러리, insort() 함수 사용
    for i in range(1,len(a)):
        bisect.insort(a,a.pop(i),0, i)


if __name__ == '__main__':
    print('이진 삽입 정렬')
    num = int(input('원소의 크기 입력해주세요 : '))
    array = [None] * num

    for i in range(num):
        array[i] = int(input(f'array[{i}] :'))

    binary_insertion_sort(array)

    print()
    print("이진삽입정렬을 수행합니다.")
    print('오름차순으로 수행합니다.')
    print()


    for i in range(num):
        print(f'array[{i}] = {array[i]}')
