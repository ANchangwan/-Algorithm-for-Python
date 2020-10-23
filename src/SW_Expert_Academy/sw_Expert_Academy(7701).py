T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())                          # 입력할 크기 입력
    name_lst = []                               # 리스트 생성
    for i in range(num):                        
        name_lst.append(input())                # 입력하면서 대입
    name_lst2 = list(set(name_lst))             # 중복값 제거
    name_lst2.sort()                            # 제거된 리스트 정렬
    name_lst3 = sorted(name_lst2, key=len)      # 길이에 따라 다시 정렬하고 새로운 객체 생성
    print('#'+str(test_case))
    for name in name_lst3:                      # 리스트 출력
        print(name)
