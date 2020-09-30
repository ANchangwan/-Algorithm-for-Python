# KMP법으로 문자열 검색하기
def kmp_match(txt:str, pat:str) ->None:
    """kmp 문자열 생성"""
    pt = 1                                  # txt 커서
    pp = 0                                  # patten 커서
    skip = [0] * (len(pat) + 1)             # 건너뛰기 표
    
    # 건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt+=1
            pp+=1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
    
    # 문자열 검색하기
    pt = pp =0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1

        elif pp == 0:
            pt += 1

        else:
            pp = skip[pp]
    
    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    txt = input('텍스트를 입력하세요 : ')
    pat = input('검색할 문자를 입력하세요 : ')

    idx = kmp_match(txt, pat)

    if idx == -1:
        print('찾고자하는 문자가 없습니다.')
    else:
        print(f"찾고자하는 문자가 있습니다. {(idx + 1)}")
