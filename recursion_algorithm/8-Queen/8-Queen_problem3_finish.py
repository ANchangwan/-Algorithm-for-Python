
board = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        for j in range(8):
            print('■'if board[i] ==j else '□',end="")
        print()
        #print(f'{board[i]:2}', end ='')
    print()
    

def set(i:0) ->None:
    """i열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if( not flag_a[j]               # j행에 퀸이 배치되지 않았다면
            and not flag_b[i + j]       # 대각선 방향으로 퀸이 배치되지 않았다면
            and not flag_c[i - j + 7]):     # 대각선 방향으로 퀸이 배치되지 않았다면
            board[i] = j                # 퀸을 j행에 배치
            if i == 7:
                put()
            else:
                flag_a[j] =flag_b[i + j] = flag_c[i- j + 7] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i - j + 7] = False

set(0)