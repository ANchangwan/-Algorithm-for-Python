# 하노이 탑 구현

def move(circleNum:int, start:int, goal:int)->int:
    if circleNum > 1:
        move(circleNum-1, start, 6-start-goal)

    print(f'원반 [{circleNum}]을 {start}기둥에서 {goal}기둥으로로 이동합니다.')

    if circleNum > 1:
        move(circleNum-1, 6-start-goal, start)

n = int(input('원반의 갯수를 입력하세요 : '))

move(n, 1, 3)