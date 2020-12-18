
for test_case in range(int(input())):
    N = int(input())
    map = [0 for _ in range(8) for __ in range(8)]
    result = 0

    def isTrue(x):
        for i in range(1,x):
            if map[x] == map[i] or abs(map[x] - map[i]) == x - i:
                return False
        return True

    def dfs(cnt):
        global result
        if cnt > N:
            result += 1
        else:
            for i in range(1, N+1):
                map[cnt] = i
                if isTrue(cnt):
                    dfs(cnt + 1)

    dfs(1)
    print(map)
    print("#{} {}".format(test_case+1, result))