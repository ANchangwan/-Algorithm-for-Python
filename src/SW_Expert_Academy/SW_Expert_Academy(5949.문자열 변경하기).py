
for test_case in range(int(input())):
    first_str = input().rstrip()
    second_str = input().rstrip()
    first = []
    second = []
    cnt = 0

    for i in range(len(first_str)):
        if first_str[i] =='a':
            first.append(i)
        if second_str[i] == 'a':
            second.append(i)

    for i in range(len(first)):
        if first[i] > second[i]:
            cnt += first[i] - second[i]
        else:
            cnt += second[i] - first[i]

    print("#" + str(test_case+1) + ' ' + str(cnt))

