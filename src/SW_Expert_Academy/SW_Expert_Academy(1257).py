# 1257 알고리즘 문제

T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    ipt = input()
    sorted_lst = []

    for i in range(len(ipt)):
        for j in range(i,len(ipt)):
            sorted_lst.append(ipt[i:j+1])
    sorted_lst2 = sorted(list(set(sorted_lst)))
    if K > len(sorted_lst2):
        lst = 'None'
    else:
        lst = sorted_lst2[K-1]
    print("#{} {}".format(test_case,lst))
