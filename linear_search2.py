from ssearch_func.search_while import seq_search2 


print('실수를 입력합니다.')
print('End를 입력하면 종료합니다.')

listNum = []
number = 0

while True:
    num = input(f'숫자를 입력하세요(listNum[{number}]) = ')
    if num == 'End' or num =='end': 
        break
    listNum.append(float(num))
    number+=1

key = int(input('찾고자 하는 값을 입력하세요. : '))

idx = seq_search2(listNum,key)

if idx == -1:
    print("찾고자하는 값이 없습니다.")

else:
    print(f"listNum[{idx}] = {listNum[idx]}")
