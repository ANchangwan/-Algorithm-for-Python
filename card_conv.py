# 10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기


def card_conv(x:int,r:int) ->str:
    """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x>0:
        d+= dchar[x % r]
        x //=r

    return d[::-1]



if __name__ == '__main__':
    while True:
        while True: # 음이 아닌 정수를 입력받음
            no = int(input('0이 아닌 정수를 입력해주세요 : '))
            if no>0:
                break
        
        while True:
            cd = int(input('어떤 진수로 변환할까요?'))
            if 2 <= cd <= 36:
                break

        
        print(f'{cd}진수로는  {card_conv(no,cd)} ')

        retry = input('한번더 변환할꺼요? (yes or no)')
        if retry in {'N','n'}:
            break
