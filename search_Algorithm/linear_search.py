from typing import Any, Sequence

def search_array(a:Sequence, key:Any) ->int:

    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1




number = 0
x = []

while True:
    s = input(f'x[{number}] : ')
    if s == 'End':
        break
    x.append(float(s))
    number+=1

key = int(input('찾고자하는 원소 값 : '))

idx = search_array(x,key)

if idx == -1:
    print("찾고자하는 원소값이 존재하지 않습니다.")
else:
    print(f"찾고자하는 원소값 x[{idx}]입니다")
