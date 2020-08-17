from enum import Enum
from Data_struct.ssearch_func import ChaineHash

Menu = Enum('Menu',['추가','삭제','검색','덤프','종료']) #메뉴를 선언

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep="  ",end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChaineHash(13)

while True:
    menu = select_menu() # 메뉴 선택

    if Menu == menu.추가:   # 추가
        key =int(input('추가할 키값을 입력하세요. : '))
        val = int(input('추가할 값을 입력하세요. : '))
        if not hash.add(key,val):
            print("추가를 실패했습니다.")
    
    elif Menu == menu.삭제:
        key = int(input('삭제할 키값을 입력하세요. : '))
        if not hash.remove(key):
            print('삭제를 실패했습니다.')
    
    elif Menu == menu.검색:
        key = int(input('검색할 키값을 입력하세요. : '))
        if not hash.search(key):
            print('검색을 실패했습니다.')

    elif Menu == menu.덤프:
        hash.dump()
    
    else:
        break
