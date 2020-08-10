# while 문으로 작성한 선형 검색 알고리즘

from typing import Any,Sequence

# 선형 검색1 
def seq_search1(a:Sequence ,key:Any) ->int:

    i = 0

    while True:
        if i == len(a):
            return -1
        elif a[i] == key:
            return i
        
        i+=1

# 선형 검색2
def seq_search2(a:Sequence,key:Any) -> int:

    for i in range(len(a)):
        if a[i] == key:
            return i

    return -1

# 코드가 간결해짐


if __name__=='__main__':

    num = int(input('원하는 원소의 갯수 : '))
    a = [None]*num

    for i in range(len(a)):
        a[i] = int(input(f'원소 a[{i}]: '))

    key = int(input('찾고자하는 키값 : '))

    idx = seq_search2(a,key)

    for i in range(len(a)):
        print(f'a[{i}] = {a[i]}')
    
    if idx == -1:
        print("찾고자하는 값이 없습니다.")
    else:
        print(f"찾고자하는 값 a[{idx}] : {a[idx]} ")