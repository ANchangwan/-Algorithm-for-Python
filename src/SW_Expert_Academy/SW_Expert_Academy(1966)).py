# 숫자를 정렬하자
T = int(input())
for test_case in range(1, T + 1):
    input()
    lst = list(map(int,input().split()))
    lst.sort()
    print("#" + str(test_case),*lst)