min_res, max_res = 1e9, -1e9

def operate(i, res, add, sub, mul, div):
    global max_res, min_res
    if i == N:
        max_res = max(res, max_res)
        min_res = min(res, min_res)
        return

    else:
        if add:
            operate(i+1, res+nums_count[i], add-1, sub, mul, div)
        if sub:
            operate(i+1, res-nums_count[i], add, sub-1, mul, div)
        if mul:
            operate(i+1, res*nums_count[i], add, sub, mul-1, div)
        if div:
            operate(i+1, int(res/nums_count[i]), add, sub, mul, div-1)

if __name__ == '__main__':
    N = int(input())
    nums_count = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    operate(1,nums_count[0], add, sub,mul,div)
    print(max_res)
    print(min_res)

