for test_case in range(int(input())):
    N = int(input())
    height = sorted(map(int,input().split()))
    result = 0
    for i in range(N-2):
        result = max(result, height[i+2]-height[i])
    print("#{} {}".format(test_case+1,result))



