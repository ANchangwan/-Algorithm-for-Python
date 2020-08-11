from typing import Any, Sequence
import copy

def seq_search(seq:Sequence, key:Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""

    a = copy.deepcopy(seq)      # seq를 복사
    a.append(key)                 # 보초 key값을 추가

    i = 0
    while True:
        if a[i] == key:
            break # 검색을 성공하면 while문을 종료합니다.
        i+=1

    return -1 if i == len(seq) else i



if __name__ == '__main__':
    num = int(input('입력할 원소 값 : ')) # num값 입력
    x = [None] * num                     # 원소 수가 num인 배열 생성 

    for i in range(num):
            x[i] = int(input(f'입력할 원소 값 x[{i}] :'))

    key = int(input('찾고자하는 카값 : ')) # 키값 입력받기

    idx = seq_search(x, key)               # 키 key값과 같은 원소를 x에서 검색

    if idx == -1:
        print("찾고자하는 인덱스값이 없습니다.")
    else:
        print(f'검색값은 x[{idx}]에 있습니다.') 