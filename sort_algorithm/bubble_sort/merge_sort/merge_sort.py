# 병합 정렬

from typing import Sequence, MutableSequence

def merge_sort(a:Sequence , b:Sequence, c:MutableSequence) -> None:
    pa, pb, pc = 0,0,0                      # 각 배열커서의위치
    na, nb= len(a), len(b)   # 각 배열의 원소 수

    while pa < na and pb < nb:
        if a[pa] <= a[pb]:
            c[pc] = a[pa]
            pa+=1
        else:
            c[pc] = b[pb]
            pb+=1
        pc+=1

    while pa < na:
        c[pc] = a[pa]
        pa+=1
        pc+=1

    while pb < nb:
        c[pc] = b[pb]
        pb+=1
        pc+=1      

if __name__ == '__main__':

    num_a = [1,8,9,11,16,2]
    num_b = [1,2,3,21,27,28]
    num_c = [None] * (len(num_a)+len(num_b))


    merge_sort(num_a, num_b, num_c)

    print(f'배열 a = {num_a}')
    print(f'배열 b = {num_b}')
    print(f'배열 c = {num_c}')