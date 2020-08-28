#유클리드 호제법으로 최대 공약수 구하기

def euclidean(x:int, y:int) ->int:
    if y ==0:
        return x
    else:
        return (y,x%y)

if __name__ == "__main__":
    print("최대 공약수 구하기")
    x = int(input('첫 번째 정숫값을 입력 : '))
    y = int(input('두 번째 정숫값을 입력 : '))

    print(f'두 정수의 최댓 공약수 : {euclidean(x,y)}')