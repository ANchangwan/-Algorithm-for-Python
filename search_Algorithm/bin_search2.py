# 이진 검색 알고리즘의 실행 과정을 출력

from typing import Any,Sequence

def bin_search2(a:Sequence, key:Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진검색(실행 과정을 출력)"""

    front = 0               # 검색 범위 맨 앞 원소의 인덱스
    end = len(a) - 1        # 검색 범위 맨 끝 원소이 인덱스

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4*len(a)+2) * '-')

    while True:
        middle = (front + end) // 2     # 중앙 원소의 인덱스

        print("   |", end='')
        if front !=middle: # front 위에 <-를 출력
            print((front * 4 + 1) * ' ' + '<-' + ((middle - front) * 4)* ' '+'+',end='')
        else:
            print((middle * 4 + 1) * ' ' + '<+', end ='')
        if middle != end:    # end 원소 위에 ->를 출력
            print(((end - middle) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{middle:3}|', end = '')
        for i in range(len(a)):
            print(f'{a[i]:4}', end ='')
        print('\n   |')


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

    a[0] = int(input('x[0] : '))

    for i in range(1,num):
        while True:
            a[i] = int(input(f'원소 a[{i}] : '))
            if a[i]>=a[i-1]:
                break
   
            
  

  
    
    key = int(input('찾고싶은 원소 값 : '))

    idx = bin_search2(a, key)

    if idx == -1:
        print('찾고자 하는 원소값이 없습니다.')
    else:
        print(f"검색 값 a[{idx}]입니다.(값 : {a[idx]}) ")