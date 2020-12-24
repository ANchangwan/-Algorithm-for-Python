import sys
import copy
from collections import deque

dx = [1,-1,0, 0]
dy = [0, 0, 1, -1]
result = 0

def bfs():
    global result
    copiedmap = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if copiedmap[i][j] == 2:
                q.append([i,j])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <=ny < M:
                if copiedmap[nx][ny] == 0:
                    copiedmap[nx][ny] = 2
                    q.append([nx,ny])

    cnt = 0
    for i in copiedmap:
        cnt += i.count(0)
    result = max(result,cnt)




def wall(x):
    if x == 3:
        bfs()
        return 
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(x+1)
                board[i][j] = 0


N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    

q = deque()
wall(0)
print(result)