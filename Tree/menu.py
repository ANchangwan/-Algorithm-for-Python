from enum import Enum
from tree_struct import BinarySearchTree

Menu = Enum('Menu', ['삽입', '삭제','검색','출력','값의 범위','종료'])


def select_menu() -> Menu:
    s = [f'{m.value} {m.name} for m in Menu']
    while True:
        print(*s,sep =' ',end= '')
        try:
            select_num = int(input(' : '))
            if 1 <= select_num <= len(Menu):
                return Menu(select_num)
        except:
            print(f"1 ~ {len(select_num)}사이에 값을 입력해주세요 ")


tree = BinarySearchTree()

while True:
    menu = select_menu()

    if menu == Menu.삽입:
        key = int(input('삽입할 키를 입력하세요 : '))
        val = input('삽입할 값을 입력해주세요 : ')
        if not tree.add(key, val):
            print('삽입할 값이 없습니다.')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력해주세요 : '))
        tree.remove(key)

    elif menu == Menu.검색:
        key = int(input('검색할 키값을 입력해주세요 : '))
        t = tree.search(key)
        if t is not None:
            print(f'값 : {t}')
            print(f'{t}를 찾았습니다.')
        else:
            print('값을 찾을 수 없습니다.')

    elif menu == Menu.덤프:
        tree.dump()

    elif menu == Menu.키의범위:
        print(f'키의 최댓값 {tree.max}')
        print(f'키의 최솟값 {tree.min}')

    else:
        break
