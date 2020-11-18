def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root1 = find(x)
    root2 = find(y)
    if root1 > root2:
        parent[root1] = root2
    else:
        parent[root2] = root1


def equl(x, y):
    return find(x) == find(y)


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(int(input())):
    cnt = 0
    V,E = map(int,input().split())
    parent = [i for i  in range(V+1)]
    edge = [list(map(int,input().split()))]
    edge.sort(key = lambda x:-x[2])
    while edge:
        a,b,c = edge.pop()
        if not equl(a,b):
            union(a,b)
            cnt+=c
    print('#{} {}'.format(test_case,cnt))