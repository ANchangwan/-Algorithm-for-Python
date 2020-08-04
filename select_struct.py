# # 예제1
# # 최댓값

# inputNum = 0
# num = []
# max = 0
# wantTocount = int(input('입력하고 싶은 수를 입력해주세요!'))
# for i in range(wantTocount):
#     inputNum = int(input('정수를 입력해주세요.: '))
#     num.append(inputNum)

# for k in num:
#     if max < k:
#         max = k

# print(f'최대값 : {max}')


# 예제2
# 최댓값
def maxValue(a):

    max = a[0]
    for i in range(0,len(a)):
        if a[i]>max:
            max = a[i]
    
    return max
if __name__ == "__main__":
    
    print('값을 입력해주세요')
    value = int(input('원소의 갯수를 입력해주세요 : '))
    x = [None] * value
    
    for i in range(value):
        x[i] = int(input(f'x[{i}]의 값을 입력해주세요 : '))
    
    print(f'최댓값은 {maxValue(x)}입니다.')
